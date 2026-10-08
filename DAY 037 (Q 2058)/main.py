class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        def code(head):
            prev = head
            temp = head.next
            pos = 2
            prev_pos = 0
            minm = float('inf')
            storage = []

            while temp.next:
                if ((prev.val < temp.val > temp.next.val) or
                    (prev.val > temp.val < temp.next.val)):

                    storage.append(pos)

                    if prev_pos != 0:
                        minm = min(minm, pos - prev_pos)

                    prev_pos = pos

                pos += 1
                prev = temp
                temp = temp.next

            if len(storage) < 2:
                return [-1, -1]

            maxm = storage[-1] - storage[0]

            return [minm, maxm]

        return code(head)
