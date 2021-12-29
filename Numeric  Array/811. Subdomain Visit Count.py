class Solution:
    def subdomainVisits(self, cpdomains: [str]) -> [str]:
        count_dict = {}
        for pair in cpdomains:
            count, website = pair.split(' ')
            subdomains = website.split('.')
            for i in range(len(subdomains) - 1, -1, -1):
                domain = '.'.join(subdomains[i:len(subdomains)])
                if count_dict.get(domain) is None:
                    count_dict[domain] = 0
                count_dict[domain] += int(count)
        res = []
        for k, v in count_dict.items():
            res.append(str(v) + " " + k)
        return res

test = Solution()
domains = ["9000 yahoo.test.com", "12345 baidu.com", "1111 columbia.test.com"]
print(test.subdomainVisits(domains))
