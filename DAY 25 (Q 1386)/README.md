# **1386. Cinema Seat Allocation**





#### A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.

#### 

#### You are given a 2D integer array reservedSeats, where reservedSeats\[i] = \[rowi, seati] means that seat seati in row rowi is already reserved.

#### 

#### A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:

#### 

#### seats 2, 3, 4, 5

#### seats 4, 5, 6, 7

#### seats 6, 7, 8, 9

#### A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.

#### 

#### Return an integer denoting the maximum number of four-person groups that can be assigned.







# **MY EXPLANATION-**





**1. We store reserved seats in a dictionary where each row maps to a set of reserved seat numbers.**

**2. We don't iterate through all `n` rows because `n` can be as large as `10⁹`.**

**3. Every row with no reserved seats can fit \*\*2 families\*\*, so we calculate those directly.**

**4. For rows with reservations, we check the three possible groups: \*\*2–5, 4–7, and 6–9\*\*.**

**5. `all()` checks whether every seat in a particular group is available.**

**6. If \*\*left and right\*\* groups are available, we can place \*\*2 families\*\* because they don't overlap.**

**7. Otherwise, if any one group is available, we place \*\*1 family\*\*, and finally return `total`.**



