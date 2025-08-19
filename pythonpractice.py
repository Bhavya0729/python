pipeline
{
   agent any
    stages 
    {
        stage('Continuous Download')
        {
            steps 
            {
                git branch: 'main', url: 'https://github.com/Bhavya0729/python.git'
            }
        }
        
        stage('Continuous Build') 
        {
            steps 
            {
                  sh 'python3 python.py'
            }
        }
        stage ('continous deployment')
         {
          steps
          {
              sh 'scp "/var/lib/jenkins/workspace/declarativepipeline-python/python.py" ubuntu@172.31.44.38:/home/ubuntu/tom'
          }
      }
       stage ('continous testing')
         {
             steps
             {
                  sh 'python3 "/var/lib/jenkins/workspace/declarativepipeline-python/python.py"'
             }
         }
         stage ('continous release')
               {
                   steps
                   {
                       sh 'scp "/var/lib/jenkins/workspace/declarativepipeline-python/python.py" ubuntu@172.31.42.163:/home/ubuntu/tom'
                   }
              }
    }
}
    
