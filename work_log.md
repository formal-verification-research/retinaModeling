
| Date     | Work
|----------|---------------------------------------------------------------
| 9/21/19  |  Created design plan for using Eq 1 from the Oncology paper to solve the Move or Stay problem. Created a new branch on github to begin modifying the model because of the new concentration function.
| 9/30/19  |  Created a new model to incorporate the new method of calculating the concentration. Calculates all necessary concentrations and chemoattractant functions and transition probabilities. Plugs everything into Eq 1 to calculate the change in pmn. The problem is that when I start with pmn=1 after one iteration pmn=0 and all directional probabilities are equally likely. There must be something wrong with my logic because I think everything in the code is correct and doing what it is supposed to. Next time I am going to try to incorporate 1/k into the transitional probabilities and see if that helps.
|          |   
|          |  
