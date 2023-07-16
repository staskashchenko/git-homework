# git-homework
Practising git workflows, branching strategies and conflict resolution techniques.

EXPLANATION OF BRANCHING STRATEGY AND WORKFLOW IMPLEMENTATION:

We have chosen to use GitHub Flow as it is simpler than GitFlow and our project is very basic.

We decided to create 4 feature branches separate from our main branch. 

We used the following command lines in the gitbash terminal to create new branches:

- git checkout main (to ensure we were first on the main branch)
- git branch feature/new-feature
- git checkout feature/new-feature

Then we used: 'git add .','git commit -m "some text here", and then finally 'git push origin feature/new-feature' to fill out each of the
branches.

Three of the branches were self-contained python functions and the fourth was a user interface which would employ
the three functions. We then worked independently on our assigned features/branches and once we were finished we merged our respective
branches with the main branch.

In order to merge the branches with main we used the following commands in the gitbash terminal:
- git checkout main (again, ensuring we were in the main branch first)
- git pull (to ensure we were working on the most up-to-date version of main)
- git merge feature/new-feature (merges the feature branch with the main branch)
- fixed any conficts manually in our IDE after consulting one another, then saving our main.py file
- git add . , git commit -m "some text here", git push origin main  (standard procedure)

 Because it was stipulated as such in the task outline, we then created a release branch following pretty much the exact same procedure we used to merge the feature branches with the main branch.

Furthermore it was necessary to employ at least one advanced github technique. We chose Git cherry-p. 
We utilised this method to fix some small bugs we had in the code, mainly banal type errors. Below is an outline of the cherry-p process:

- first, we used 'git checkout feature/feature-to-change' (so we were in the right branch to make changes)
- second, we made any changes, commited and pushed them (standard process)
- third, we used 'git log --oneline' (so that we could get the right commit hash)
- fourth, we used 'git checkout release' and then git pull (to change to the release branch, and have the latest version)
- fifth, 'git cherry-pick <commit-hash>' (we then made the necessary changes to main.py to resolve conflicts)
- sixth, 'git cherry-pick --continue' (this would often open up a window which we could use to add a commit message)
- seventh, the usual git commit and git push origin release.

But in all honesty for such a small project with just two people it was kinda overkill and not really helpful. Regular merging was more than enough for our needs. 
