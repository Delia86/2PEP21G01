import subprocess
from subprocess import Popen,run,CompletedProcess
from subprocess import SubprocessError

result=run(['dir'],shell=True,text=True,capture_output=True)

# print(type(result))
# #print(result.stdout)
#
#
# result=run(['ping' ,'8.8.8.8'],text=True,capture_output=True)
# print(type(result))
# #print(result.stdout)

# result=Popen(['ping','8.8.4.4'],text=True,  stderr= subprocess.PIPE)
# result=Popen(['ping','8.8.4.4'],text=True,  stout= subprocess.PIPE)
# stdout,stderr=result.communicate()
# print(f'Stdout:{stdout}')
# print(f'Stdout:{stderr}')
# print(type(result))
# print(result.stdout)

# result=Popen(['pingx'],text=True,stdout=subprocess.PIPE)
# stdout,stderr=result.communicate()

result=Popen(['ping','8.8.4.4','-n','1'],text=True, stderr=subprocess.PIPE)
stdout,stderr=result.communicate()

print(type(result))


