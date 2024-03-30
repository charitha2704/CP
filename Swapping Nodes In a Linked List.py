class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        rightPos=head
tmp=head
leftCount=1;
    while tmp:
        if leftcount<k:
            leftCount+=1
            leftPos=leftPos.next
        else:
            if tmp.next:
                rightPos=rightPos.next
            tmp=tmp.next
        leftPos.val,rightPos.val=rightPos.val,leftPos.val
    return head
