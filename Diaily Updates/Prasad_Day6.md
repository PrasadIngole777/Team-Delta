Git Commands and Their Function : 

1)

      git init : Initializes a new Git repository in the current directory.
2) 

       git clone <url>: Creates a local copy of a remote repository located at the URL.
3) 

       git add <file>: Stages a change made to a file for the next commit.
4)

      git commit -m "<message>": Records the staged changes as a new commit with a descriptive message.
5)

    
      git push <remote> <branch>: Uploads all local commits to the specified remote repository and branch.
6) 

       git branch: Lists all local branches in the current repository.
7) 

       git branch <new_branch>: Creates a new local branch.
8)

      git merge <branch>: Merges the specified branch into the current branch.
9)

      git pull: Fetches and merges any changes from the remote repository into the current local repository.
10) 

        git status: Shows the current status of the repository, including any changes not yet staged.
11)

        git diff: Shows the differences between the current file and the last commit.
12)

        git reset <commit>: Unstages all changes made after the specified commit.


Techniques for Branching, Merging, and Conflict Resolution
  Branching
      
      git branch [branch-name]: Creates a new branch.
      git checkout -b [branch-name]: Creates a new branch and switches to it.
      git branch: Lists all branches.
      git branch -d [branch-name]: Deletes a branch.
      
  Merging
      
      Fast-forward Merge: If the branch to be merged in is ahead of the current branch with no other changes.
      git merge [branch-name]: Merges the specified branch into the current branch.
      Three-way Merge: When the current branch has diverged from the branch to be merged.
      git merge [branch-name]: Merges the specified branch into the current branch, creating a new commit.
