class Solution:
    def numberToWords(self, num: int) -> str:
        # Check for the zero case explicitly
        if num == 0:
            return 'Zero'

        # Words for numbers less than 20
        less_than_20 = [
            '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
      
        # Tens place words
        tens = [
            '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]
        
        def translate(num):
            if num == 0:
                return ''
            elif num < 20:
                return less_than_20[num] + ' '
            elif num < 100:
                return tens[num // 10] + ' ' + translate(num % 10)
            elif num < 1000:
                return less_than_20[num // 100] + ' Hundred ' + translate(num % 100)
            elif num < 1000000:
                if translate(num % 1000):
                    return translate(num // 1000) + ' Thousand ' + translate(num % 1000)
                else:
                    return translate(num // 1000) + 'Thousand'
            else:
                if translate(num % 1000_000):
                    return translate(num // 1000000) + ' Million ' + translate(num % 1000000)
                else:
                     return translate(num // 1000000) + 'Million'
            
        return translate(num)
    
s = Solution()
print(s.numberToWords(1232545677))