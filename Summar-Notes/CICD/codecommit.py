


# AWS CodeCommit
    # It is a secure, highly scalable, managed source control service that hosts private Git repositories. It 
    # makes it easy for teams to securely collaborate on code with contributions encrypted in transit and at rest. 
    # CodeCommit eliminates the need for you to manage your own source control system or worry about scaling its 
    # infrastructure. You can use CodeCommit to store anything from code to binaries. It supports the standard 
    # functionality of Git, so it works seamlessly with your existing Git-based tools.
# With CodeCommit, you can:
    # Benefit from a fully managed service hosted by AWS. CodeCommit provides high service availability and durability 
    # and eliminates the administrative overhead of managing your own hardware and software. There is no hardware 
    # to provision and scale and no server software to install, configure, and update.
    # Store your code securely. CodeCommit repositories are encrypted at rest as well as in transit.
    # Work collaboratively on code. CodeCommit repositories support pull requests, where users can review and comment 
    # on each other's code changes before merging them to branches; notifications that automatically send emails to users 
    # about pull requests and comments; and more.
    # Easily scale your version control projects. CodeCommit repositories can scale up to meet your development needs. 
    # The service can handle repositories with large numbers of files or branches, large file sizes, and lengthy revision 
    # histories.
    # Store anything, anytime. CodeCommit has no limit on the size of your repositories or on the file types you can 
    # store.
    # Integrate with other AWS and third-party services. CodeCommit keeps your repositories close to your other production 
    # resources in the AWS Cloud, which helps increase the speed and frequency of your development lifecycle. It is 
    # integrated with IAM and can be used with other AWS services and in parallel with other repositories. For more 
    # information, see Product and service integrations with AWS CodeCommit.
    # Easily migrate files from other remote repositories. You can migrate to CodeCommit from any Git-based repository.
    # Use the Git tools you already know. CodeCommit supports Git commands as well as its own AWS CLI commands and APIs.
# Using repository notification rules
    # Configuring notification rules helps your repository users by sending emails when someone takes an action that 
    # affects another user. For example, you can configure a notification rule to send notifications when comments are 
    # made on commits. In this configuration, when a repository user comments on a line of code in a commit, other 
    # repository users receive an email. They can sign in and view the comment. Responses to comments also generate emails, 
    # so repository users stay informed.
    # Notification rules are different from repository triggers, and they are also different than the notifications you 
    # could configure in the CodeCommit console before November 5, 2019.
    # Although you can configure a trigger to use Amazon SNS to send emails about some repository events, those events 
    # are limited to operational events, such as creating branches and pushing code to a branch. Triggers do not use 
    # CloudWatch Events rules to evaluate repository events. They are more limited in scope. 
# Authentication
    # To use CodeCommit, you configure your Git client to communicate with CodeCommit repositories. As part of this 
    # configuration, you provide IAM credentials that CodeCommit can use to authenticate you. IAM supports CodeCommit 
    # with three types of credentials:
    # Credential Types
        #(1) Git credentials, an IAM-generated user name and password pair you can use to communicate with CodeCommit 
        # repositories over HTTPS.
        #(2) SSH keys, a locally generated public-private key pair that you can associate with your IAM user to communicate 
        # with CodeCommit repositories over SSH.
        #(3)  AWS access keys, which you can use with the credential helper included with the AWS CLI to communicate with 
        # CodeCommit repositories over HTTPS.