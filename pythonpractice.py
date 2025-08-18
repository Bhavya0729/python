pipeline
{
   agent any
    stages 
    {
        stage('Continuous Download')
        {
            steps 
            {
                git branch: 'main', url: 'https://github.com/Surja07/python.git'
            }
        }
        
        stage('Continuous Build') 
        {
            steps 
            {
                  sh 'python3 Python.py'
            }
        }
        
            stage ('continous deployment')
         {
          steps
          {
              sh 'scp "/var/lib/jenkins/workspace/Declaritive pipeline2/Python.py" ubuntu@172.31.9.223:/var/lib/tomcat10/webapps/'
          }
      }
      
        stage ('continous testing')
         {
             steps
             {
                  sh 'python3 "/var/lib/jenkins/workspace/Declaritive pipeline2/Python.py"'
             }
         }
         
        stage ('continous release')
               {
                   steps
                   {
                 sh 'scp "/var/lib/jenkins/workspace/Declaritive pipeline2/Python.py" ubuntu@172.31.12.169:/var/lib/tomcat10/webapps/'
                   }
              }
     }
}
