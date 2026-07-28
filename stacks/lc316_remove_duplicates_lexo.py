class Solution(object):
    def removeDuplicateLetters(self, s):
    
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                continue  # already placed, skip this occurrence

            # Remove from stack top while: it's bigger than current char,
            # AND it reappears later (so removing it now is safe)
            # Maintain lexicographical order:
            # Pop larger characters from the stack IF they appear later in the string

            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)
        return "".join(stack)