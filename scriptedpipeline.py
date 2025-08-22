node('built-in')
{
stage('continuous download')
{
    git branch: 'main', url: 'https://github.com/Bhavya0729/python.git'
}
 stage('Continuous Build') 
            {
                  sh 'python3 python.py'
            }
        stage ('continous deployment')
          {
              sh 'scp "/var/lib/jenkins/workspace/scriptedpipepy/python.py" ubuntu@172.31.44.38:/home/ubuntu/ten'
          }
      stage ('continous testing')
             {
                  sh 'python3 "/var/lib/jenkins/workspace/scriptedpipepy/python.py"'
             }
         
         stage ('continous release')
                   {
                       sh 'scp "/var/lib/jenkins/workspace/scriptedpipepy/python.py" ubuntu@172.31.42.163:/home/ubuntu/ten'
                   }
              }
