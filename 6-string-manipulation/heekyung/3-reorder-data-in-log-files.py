class Solution:
    '''
    로그 재정렬
    1. 로그의 가장 첫번째 단어는 식별자
        문자 로그 - 소문자 영어로만 이루어짐
        숫자 로그 - 숫자들로 이루어짐
    2. 문자 로그는 모든 숫자 로그보다 앞에 온다
    3. 문자 로그는 각 내용의 사전순으로 정리하며 순서가 동일할 경우  로그 식별자 순으로 한다.
    4. 순자로그는 현재 순서를 유지한다.

    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    Explanation:
    The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
    The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
    '''
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def func(s):
            return s.split()[1:], s.split()[0]

        letter_logs = []
        digit_logs= []

        for log in logs:

            # 숫자로그이면
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # 문자로그를 두개의 키로 정렬
        letter_logs.sort(key=lambda s: (s.split()[1:]. s.split()[0]))
        # 함수로 대체 가능
        #letter_logs.sort(key=lambda s: (s.split()[1:].s.split()[0]))

        # 리스트 더해서 반환
        return letter_logs + digit_logs