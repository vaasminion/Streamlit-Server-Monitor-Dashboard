import subprocess
import os
def ping_check(host, count=1):
  """Pings a server and returns True if successful, False otherwise.

  Args:
      host: The hostname or IP address of the server.
      count: The number of pings to send (default: 1).

  Returns:
      True if the ping was successful, False otherwise.
  """
  param = '-c' if os.name == 'posix' else '-n'  # Adjust for OS compatibility
  command = f"ping {param} {count} {host}"
  #result = subprocess.run(command.split(), capture_output=True)
  result = subprocess.run(command,capture_output=True,shell=True)

  return result.returncode == 0