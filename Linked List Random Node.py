class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.stack=head
        self.curPointer=head
        self.counter=0
        while self.curPointer:
            self.counter=1
            self.curPointer=self.curPointer.next

    def getRandom(self) -> int:
        n=random.uniform(0,self.counter)
        self.curPointer=self.stack
        while n>1:
            self.curPointer=self.stack
            n-=1
        return self.curPointer.val
