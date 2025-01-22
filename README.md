# capgemini-challenge-repo
 Capgemini Technical Interview 
 Contains the source code sampler.py originally for Capgemini's technical interview proccess.
 


# View my thought proccess for each question:


Question 1: relative_to_common_base

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
        
        THE IN THE ACTUAL FUNCTION:
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

        Test Cases:
            Daniel's test cases passes.
            My test case passes:
                at_time = 5, What is the vehicle's speed at the time stamp of 5
                My points are point (0,0) and point (0,10)
                Distance= √((0−0)^2+(10−0)^2) = 10
                Our distance is 10
                

​