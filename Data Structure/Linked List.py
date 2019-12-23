class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def Reverse(self,head):
        prev = None 
        while head:
            next = head.next
            head.next = prev;
            prev = head
            head = next
        return prev  


def Reverse(head):
    prev = None 
    while head:
        next = head.next
        head.next = prev;
        prev = head
        head = next
    return prev  
 
'''
快慢指標兩種應用
1.判斷是否為cycle  (leetcode 141)
2.取出ListNode 中間的結點 (leetcode 876)

''' 
def hasCircle(head):
    slow,fast = head ,head    
    while fast and fast.next :
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
        
    return False
    
    
    
    
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print (Reverse(head))


