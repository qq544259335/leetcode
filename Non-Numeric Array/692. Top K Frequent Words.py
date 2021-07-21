class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        words_freq_dict = {}
        for word in words:
            if word not in words_freq_dict:
                words_freq_dict[word] = 0
            words_freq_dict[word] += 1
        words_list = []
        freq_list = []
        for key in words_freq_dict:
            words_list.append(key)
            freq_list.append(words_freq_dict[key])
        self.fastSortK(words_list,freq_list,k,0,len(words_list) -1)
        target = freq_list[k - 1]
        res = []
        pre = freq_list[0]
        sort_start = 0
        sort_end = 0
        freq_list.append(-100)
        for i in range(len(freq_list)):
            # print(pre, freq_list[i])
            if pre == freq_list[i]:
                sort_end += 1
            else:
                # print(sort_start,sort_end,words_list)
                temp = words_list[sort_start:sort_end]
                temp.sort()
                words_list[sort_start:sort_end] = temp
                # print(words_list)
                sort_start = i
                sort_end = i + 1
            pre = freq_list[i]
        freq_list = freq_list[:-1]
        for idx in range(0, k):
            res.append(words_list[idx])
        return res

    def fastSortK(self,words_list:[str], freq_list:[int], k, start, end):
        if start < end:
            sep = self.partition(words_list,freq_list, start,end)
            self.fastSortK(words_list, freq_list, k, start, sep - 1)
            self.fastSortK(words_list, freq_list, k, sep + 1, end)

    def partition(self, words_list:[str], freq_list:[int], start, end):
        i = start
        target = freq_list[end]
        for j in range(start, end):
            if freq_list[j] > target:
                freq_list[j], freq_list[i] = freq_list[i], freq_list[j]
                words_list[j], words_list[i] = words_list[i], words_list[j]
                i = i + 1
        freq_list[end], freq_list[i] = freq_list[i], freq_list[end]
        words_list[end], words_list[i] = words_list[i], words_list[end]
        return i


sol = Solution()
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(sol.topKFrequent(words,k))