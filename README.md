# capgemini-challenge-repo
 Capgemini Technical Interview 
 Contains the source code sampler.py originally for Capgemini's technical interview proccess.
 


# View my thought proccess for each question:


Question 1: relative_to_common_base

    I am assuming that the input will always be that they first start of from them same folder i.e that the would both have the same relative path then some how start to diverge, so you would only need to provide where the path changes from path 2

    So for example in the test case

    /home/daniel/git/ws/py311/test.yaml (input 1)
    /home/daniel/git/slippers (input 2)

    since after git/, input two is now different, it should out put ws/py311/test.yaml since it is not relative anymore

    !PLEASE NOTE I HAD TO CHANGE THE TEST CASE TO WindowsPath() as expected as I am working with windows, should work by changing it to Posix()

Question 2: closest_word:

    This question felt pretty ambiguous as I did not know what the question meant by "most-like", since the example was
    matching for an exact match. Initially there were two approaches that I could think of, one was if the question was only looking
    for the exact match, then a simple:

        my_word = 'Python'
        for i in possibilities:
            if i == 'Python':
                bla bla bla 
        and so on... I stopped midway trying to implement this.

    However, what if there are two ? Then the test should expect multiple answers right? So we can assume that "most-like" could mean that it's either between the exact word and the most similar word, so we would need to rank each word within the list, return which word has the highest similarity.

    Therefore, we can just use a simple approach to LCS, I am assuming the challenge isn't bothered if I use a Naive vs DP implementation since the data set I am working with is small, therefore the naive recursive solution should be enough so:

        LET THE LCS LENGTH BE -1
        IF the length of the word AND the length of the word in list[index.length()] IS ZERO
        THEN
            RETURN 0 (since theres nothing to match it to)
        ELSE IF word[length-1] == list[index[length-1]]
            LCS LENGTH + 1 AND MAKE A CALL TO THE REMAINING CHARS OF THE WORD 
        ELSE (NO MATCH)
            EXCLUDE THE LAST CHARACTER OF BOTH STRINGS, TAKE THE MAXIMUM RESULT
        
        IN THE ACTUAL FUNCTION:
            loop through the list, call lcs on word and the list[index]
            update the length and close word if a longer LCS is found, if it finds it then finish.



Question 3 speed_at_time:

    Breaking down the question:

        The task at hand is simply, What is the vehicle's speed at i.e. 10 Seconds.
        What the question provides:
            -> Car travels along a path, represented by (x,y,t) where x,y are the points, and t is the timestamp
            -> Vehicle travels at a straight line, the care passes through each point at corresponding time stamps
       
        Working with this information we need to do the following:
            1. Calculate distances between two points using euclidian distance (D = srt(( x 2 − x 1 )^2 + ( y 2 − y 1 )^2))
            2. Find the total time, which is ts, as given
            3. Calculate the speed by s = d/t (note theres an if statement, i don't want to cause a divide by zero error)
        
    New logic:
        Although this works, I have forgot that I need to account for the fact that the question is asking to find the speed at 
        the time specified in at_time

            ** Therefore, I would have to take in to consideration, the position of the car at 5 seconds which leads to a new problem:
                -> How do we calculate the position of the car at say at_time = 10? We can already

            Considering the above, we already know how to get the total time, since we have the starting and ending timestamps, using the same idea,
            we would need to calculate the how much time has passed/total time from start to at_time. then calculate the proprotion, i.e where the vehicle is on its path 
            at a given time.

            Reference:
                Total time would be the whole journey
                Elapsed would be how long Ive been travelling i.e how long car has been driving on the path
                Proportion, how much have i covered,
                    Therefore let p (proportion) = e (elapsed) / t (total time)
                    Which would give us the ratio / proprotion of the travel from point 1 to the perceived point 2 is at 5 seconds

                Assumption:
                    -> Since it is a straight line, I am safe to assume that we are travelling across the lline linearly, potentially letting us use
                        linear interpolation to figure out where we are during at_time 5

                        Reference again:
                            Let linear interpolation (y) = y1 + (x-x1)*(y2-y1)/(x2-x1)

                        There fore let
                            start.x (y1) end.x (y2) (where the path starts and ends)
                            x = at_time, x1 = start.ts, x2 = end.ts
                                and respectivley for the interpolation of y