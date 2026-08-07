class Solution:
    def smallestNumber(self, num, t) :
        # 1. Verify t only contains single-digit prime factors (2, 3, 5, 7)
        temp_t = t
        for p in (2, 3, 5, 7):
            while temp_t % p == 0:
                temp_t //= p
        if temp_t > 1:
            return "-1"

        # Count total prime factors needed for t
        def get_factors(val):
            counts = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in (2, 3, 5, 7):
                while val % p == 0:
                    counts[p] += 1
                    val //= p
            return counts

        t_factors = get_factors(t)
        digit_factors = {d: get_factors(d) for d in range(1, 10)}

        # Helper to find minimum positions required to fulfill factor counts
        def min_digits_needed(req):
            r2, r3, r5, r7 = max(0, req[2]), max(0, req[3]), max(0, req[5]), max(0, req[7])
            count = r5 + r7
            
            # Pack 3s into 9s
            count_9 = r3 // 2
            rem_3 = r3 % 2
            
            # Pack 2s into 8s
            count_8 = r2 // 3
            rem_2 = r2 % 3
            
            # Combine leftovers optimally
            if rem_3 == 1 and rem_2 >= 1:
                count += 1  # 6
                rem_2 -= 1
                rem_3 = 0
            elif rem_3 == 1:
                count += 1  # 3
                rem_3 = 0
                
            if rem_2 == 2:
                count += 1  # 4
            elif rem_2 == 1:
                count += 1  # 2
                
            return count + count_9 + count_8

        # Helper to construct the smallest possible matching tail string
        def make_smallest_suffix(req, length):
            r2, r3, r5, r7 = max(0, req[2]), max(0, req[3]), max(0, req[5]), max(0, req[7])
            suffix = []
            
            while r5 > 0: suffix.append(5); r5 -= 1
            while r7 > 0: suffix.append(7); r7 -= 1
            while r3 >= 2: suffix.append(9); r3 -= 2
            while r2 >= 3: suffix.append(8); r2 -= 3
            
            if r3 == 1 and r2 >= 1: suffix.append(6); r2 -= 1; r3 -= 1
            elif r3 == 1: suffix.append(3); r3 -= 1
            
            if r2 == 2: suffix.append(4)
            elif r2 == 1: suffix.append(2)
            
            while len(suffix) < length:
                suffix.append(1)
                
            suffix.sort()
            return "".join(map(str, suffix))

        n = len(num)
        
        # 2. Track prefix factor counts
        prefix_factors = [{2: 0, 3: 0, 5: 0, 7: 0} for _ in range(n + 1)]
        first_zero = -1
        
        for i, char in enumerate(num):
            d = int(char)
            if d == 0 and first_zero == -1:
                first_zero = i
            
            for p in (2, 3, 5, 7):
                prefix_factors[i + 1][p] = prefix_factors[i][p]
            if d > 0:
                for p in (2, 3, 5, 7):
                    prefix_factors[i + 1][p] += digit_factors[d][p]

        # 3. Check if the original string matches without modification
        if first_zero == -1:
            if all(prefix_factors[n][p] >= t_factors[p] for p in (2, 3, 5, 7)):
                return num

        # 4. Scan backwards to find the optimal mutation point
        limit = first_zero if first_zero != -1 else n - 1
        
        for i in range(limit, -1, -1):
            curr_digit = int(num[i])
            space_after = n - 1 - i
            
            for d in range(curr_digit + 1, 10):
                needed = {}
                for p in (2, 3, 5, 7):
                    needed[p] = t_factors[p] - prefix_factors[i][p] - digit_factors[d][p]
                
                if min_digits_needed(needed) <= space_after:
                    return num[:i] + str(d) + make_smallest_suffix(needed, space_after)

        # 5. Fallback: If same length is impossible, increase the length by 1
        target_len = n + 1
        while True:
            if min_digits_needed(t_factors) <= target_len:
                return make_smallest_suffix(t_factors, target_len)
            target_len += 1


        # This code which i wrote Gets Anser but TLE for Larget Input t and samller input num , So we did DFS BAck Tracking Approch Which I didnt learn Yet 

        # result=""

        # # If t consist Prime factors > 7 , then no number digit products above n can be div by t , coz didgits 0->9 

        # # Factoriztion of t 
        # primes=(2,3,5,7)
        # test=t
        # i=0
        # while i < len(primes) :
        #     while test % primes[i] == 0 :
        #         test = test//primes[i]   
        #     i+=1
        # if test!=1 :
        #     return "-1"
            
        # n=int(num)

        # while True :
        #     k=n
        #     prod=1
        #     while k!=0:
        #         prod *= k%10
        #         k=k//10

        #     if  prod!=0 and prod%t==0 : # if num consists 0 , prod becomes 0 
        #         return str(n)
        #     else :
        #         n+=1