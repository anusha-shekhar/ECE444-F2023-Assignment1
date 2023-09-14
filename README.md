# Anusha Shekhar

## Activity 1: Creating a repo in your own GitHub account and committing files
- My name is a heading in this markdown file
- A screenshot of the commit on GitHub is provided below

![activity 1.2: include image of commit on GitHub](./images/name_as_heading_commit.png)

## Activity 2: Branching and merging
- A branch named "develop" was created
- The file "helloworld.py" was created in the develop branch to print "Hello World" to the terminal
- The changes were merged into the main branch
- A screenshot of the output of the merge command is provided below

![activity 2.2: include image of merge branch output on GitHub](./images/merge_output.png)

## Activity 3: Issues, pull requests and merge conflicts
- An issue has been created about adding how many years I have been at UofT
- On the main branch, "helloworld.py" now prints my name
- On the develop branch, "helloworld.py" now prints the number of years I have been at UofT
- A pull request was created, the issue created above was linked, and the merge conflicts were resolved
- A screenshot of the successful merge is provided below
  
![activity 3.3: include image of successful merge on GitHub](./images/successful_merge.png)

## Activity 4: Unit test
- The utlis class has been created in utils.py with functions named reversed and formatter
- A screenshot of the sucessful commit is provided below:
![activity 4.1: include image of commit](./images/utils_commit.png)
- A test_utils class has been created in utils_test.py with unit tests 
![activity 4.2: include image of commit](./images/utils_test_commit.png)

## Activity 5: Git rebase
- A rebase branch was created from the develop branch
- Commits c1 and c2 were made on the rebase branch:
![activity 5.1: include image of commit c1](./images/commit_c1.png)
![activity 5.2: include image of commit c2](./images/commit_c2.png)
- Commits c3 and c4 were made on the develop branch:
![activity 5.3: include image of commit c3](./images/commit_c3.png)
![activity 5.4: include image of commit c4](./images/commit_c4.png)
- Branch 'rebase' was rebased into branch 'develop' to get order of commits c1->c2->c3->c4
![activity 5.5: rebased rebase into develop](./images/git_rebase_command.png)
- The order of commits in the develop branch was changed to c3->c4->c1->c2 using the interactive rebase tool:
![activity 5.6: order of commits in interactive tool](./images/rebase_done_interactive_tool.png)
- The commits are now in the requried order:
![activity 5.7: correct order of commits](./images/rebased_git_log.png)
- The develop branch was pushed after resolving some conflicts:
![activity 5.8: develop push conflicts](./images/develop_push_error.png)
![activity 5.9: develop push success](./images/develop_resolved_push.png)
- The rebase branch was pushed:
![activity 5.10: rebase push success](./images/rebase_push.png)