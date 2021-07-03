class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = (dividend < 0) is not (divisor < 0) # look if the result of the division is negative
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0
        sub = divisor
        pow_2 = 1

        # The idea is to substract at each step the dividend by a multiple of the divisor.
        # If the multiple is too big (else condition), then we downsize the multiple of the divisor by 1 multiple,
        # and we look if we can substract the rest of the dividend by the updated multiple.
        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub # we substract the dividend by a multiple of the divisor
                res += pow_2 # Basically we add the number of mutliple of the divisor we were able to substract from the dividend

                # left shif <=> x2
                pow_2 <<= 1 # pow_2 is a power of 2
                sub <<= 1 # sub is always a multiple of the dividend
            else:
                # right shif <=> /2
                sub >>= 1
                pow_2 >>= 1

        if negative:
            res = -res
            return max(res, -2147483648)
        else:
            return min(res, 2147483647)





