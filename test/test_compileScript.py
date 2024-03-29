import asyncio
import os
import time

import pytest

from helper.Sshd import Sshd
from utils.randString import generate_random_string
from utils.logger import get_logger

logger = get_logger("CompileScript")


class TestCompileScript:
    @classmethod
    def __int__(cls, loop, script_bin):
        cls.loop = loop

    @pytest.mark.parametrize("toolchain, compiletype", [
        ("nervos/ckb-riscv-gnu-toolchain:xenial", "riscv64-unknown-elf-gcc"),
        ("docker.io/xxuejie/ckb-contract-toolchains:20230331-2", "riscv64-ckb-elf-gcc")
    ])
    def test_generateScriptBinByToolChain(self, toolchain, compiletype):
        container_name = generate_random_string(5)
        scripts_dir = os.path.abspath(os.path.join(os.getcwd(), "data/scripts"))
        # 获取目标目录下的所有文件名
        file_names = []
        for filename in os.listdir(scripts_dir):
            if filename.endswith(".c"):
                file_names.append(filename)
        for script_name in file_names:
            script_bin = script_name + "-" + compiletype + "Bin"
            os.environ['Bin'] = script_bin

            try:
                self.loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self.loop)
                asyncio.run(
                    Sshd.execute("docker", ["run", "-itd", "--name", f"{container_name}", "-v", f"{scripts_dir}:/code",
                                            f"{toolchain}", "bash"]))
                time.sleep(30)
                asyncio.run(Sshd.executeByString(
                    f"docker exec -itd {container_name} sh -c ' cd code/ && {compiletype}  -Os {script_name} "
                    f"-o {script_bin}'"
                ))
            except RuntimeError as e:
                logger.error(f"Error run: {e}")
            finally:
                self.loop.close()
                Sshd.execute_sync("make install")
                Sshd.execute_sync("make ci")
