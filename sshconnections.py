import subprocess
import logging
from ruxit.api.base_plugin import BasePlugin

class SSHConnections(BasePlugin):
    def query(self, **kwargs):
        if self.config['debug']:
            self.logger.setLevel(logging.DEBUG)
            

        self.logger.debug("SSH Connections - Starting Query... \n")
        output = subprocess.check_output("ss | grep -i ssh | wc -l", shell=True).strip()

        if self.config['debug']:
            debugOutput = subprocess.check_output("ss | grep -i ssh | awk '{print OFS FS $2 $5 $6}'", shell=True).strip()
            self.logger.debug("SSH Connections - ss output: " + str(debugOutput) + "\n")

        ssh_connects = int(output.decode("utf-8"))
        self.results_builder.absolute(key='ssh_connections', value=ssh_connects)