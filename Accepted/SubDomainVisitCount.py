class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:

        domainDict = {}
        returnList = []

        for item in cpdomains:
            domainName = ""
            number = ""
            item.strip()

            for letter in item:
                if letter.isnumeric():
                    number += letter
                elif letter.isalpha() or letter == ".":
                    domainName +=letter

            
            domainList = domainName.split(".")


            for i in range (len(domainList)-1,-1,-1):
                domain = domainList[i:len(domainList)]
                temp = ".".join(domain)
                if temp not in domainDict:
                    domainDict[temp] = int(number)
                else:
                    domainDict[temp] += int(number)
            
        for key in domainDict:
            returnList.append(str(domainDict[key]) + " " + key)
            
        return returnList
                
            



#cpdomains = ["900 google.mail.com"]
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
s = Solution()
print(s.subdomainVisits(cpdomains))