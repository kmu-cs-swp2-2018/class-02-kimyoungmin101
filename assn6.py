nt(numStr)
    except:
        return 'Error!'
    list1 = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    list2 = ['CM','CD','XC','XL','IX','IV']
    nDic = {'CM':900, 'M':1000, 'CD':400, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, 'XC':90, 'XL':40, 'IX':9, 'IV':4}
    n = 0

    for i in range(len(list2)):
        if(list2[i] in s):
            n += nDic[list2[i]]
            A = s.find(list2[i])
            for k in range(len(s)):
                s = s[A+2:]
                break;
            elif(list1[i] in s):
                n += nDic[list1[i]]
                A = s.find(list1[i])
                for k in range(len(s)):
                    s = s[A+1:]
                    break;
    return n
