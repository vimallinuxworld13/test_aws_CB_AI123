pipeline {
    agent any

   

    stages {
        stage('Trigger CodeBuild') {
            steps {
                sh 'aws codebuild start-build --project-name LWweb123 --source-version master --region ap-south-1'
            }
        }
    }

}

