class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest=secondlargest=0
        smallest=secondsmallest=float('inf')

        for n in nums:
            if n < smallest:
                secondsmallest=smallest
                smallest=n
            elif n<secondsmallest:
                secondsmallest=n
            
            if n>largest:
                secondlargest=largest
                largest=n
            elif n>secondlargest:
                secondlargest=n
        return(largest*secondlargest)-(smallest*secondsmallest)
