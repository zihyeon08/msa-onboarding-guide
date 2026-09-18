# Contributor URL 만들기

Community Influencer 활동에서 공유할 Microsoft 콘텐츠에 Student Ambassadors Contributor ID를 붙이면, 내 링크를 통해 유입된 방문을 추적할 수 있습니다. 이 문서는 원본 콘텐츠 URL을 활동에 사용할 Contributor URL로 바꾸는 방법을 정리합니다.

> 이 안내는 Community Influencer 경로의 콘텐츠 공유를 위한 문서입니다.

## 1. 먼저 Contributor ID 확인하기

등록 후 3~5일 이내에 이메일로 받은 **Student Ambassadors Contributor ID**를 사용하세요. 일반적인 형식은 다음과 같습니다.

```text
?wt.mc_id=studentamb_######
```

`######` 부분에는 본인의 고유 숫자가 들어갑니다. Learn 프로필 설정에서 보이는 **Learn Contributor ID**와 혼동하지 마세요.

## 2. 기본 URL에 Contributor ID 붙이기

URL에 물음표(`?`)가 아직 없다면, URL 끝에 Contributor ID를 그대로 붙입니다.

1. 공유할 적격 Microsoft 콘텐츠를 엽니다.
2. 주소에서 언어-지역 코드(`/en-us/`, `/ko-kr/` 등)를 제거합니다. 예를 들어 `https://learn.microsoft.com/en-us/copilot`을 `https://learn.microsoft.com/copilot`으로 바꿉니다.
3. URL 끝에 `?wt.mc_id=studentamb_######`를 붙입니다.

```text
원본:  https://learn.microsoft.com/en-us/copilot
수정:  https://learn.microsoft.com/copilot?wt.mc_id=studentamb_######
```

## 3. 기존 파라미터가 있는 URL 수정하기

원본 URL에 이미 `?`가 있다면 물음표를 하나 더 쓰지 않습니다. 기존 파라미터는 유지하고, 끝에 `&wt.mc_id=studentamb_######`를 추가합니다.

```text
원본:  https://learn.microsoft.com/en-us/copilot?WT.mc_id=academic
수정:  https://learn.microsoft.com/copilot?WT.mc_id=academic&wt.mc_id=studentamb_######
```

기존 URL에 다른 Contributor ID가 포함되어 있다면 그것을 지우지 말고, `&` 뒤에 Student Ambassadors Contributor ID를 추가하세요.

## 4. Fragment(`#`)가 있는 URL 수정하기

URL에 `#`로 시작하는 화면 위치 정보가 있다면 Contributor ID를 `#` 뒤에 붙이지 않습니다. fragment 앞의 query string에 ID를 추가합니다.

```text
원본:  https://learn.microsoft.com/copilot#overview
수정:  https://learn.microsoft.com/copilot?wt.mc_id=studentamb_123456#overview
```

기존 query string과 fragment가 모두 있다면 다음과 같이 수정합니다.

```text
원본:  https://learn.microsoft.com/copilot?view=latest#overview
수정:  https://learn.microsoft.com/copilot?view=latest&wt.mc_id=studentamb_123456#overview
```

## 5. 공유 전 최종 확인

- [ ] Student Ambassadors Contributor ID를 사용했나요?
- [ ] `learn.microsoft.com/en-us/` 같은 언어-지역 코드를 제거했나요?
- [ ] URL에 `?`가 이미 있으면 `&wt.mc_id=...`를 사용했나요?
- [ ] `#` fragment가 있다면 Contributor ID를 fragment 앞에 넣었나요?
- [ ] Community Influencer에 적합한 Microsoft URL의 콘텐츠인가요?
- [ ] Microsoft 홈페이지가 아닌 커뮤니티에 유용한 구체적인 콘텐츠인가요?
- [ ] Bitly(비틀리)와 같은 제3자 URL 단축기를 사용하지 않았나요?
- [ ] 링크를 공개 소셜 네트워크에 큐레이션한 설명과 함께 공유했나요?

링크를 만든 뒤 주소창에 전체 URL을 붙여 넣어 콘텐츠가 정상적으로 열리는지 확인하세요. Preferred Visitors 카운트는 활동 직후가 아니라 주간 리포팅 이메일과 Progression Board에 반영될 때 확인할 수 있으며, 최대 48시간이 걸릴 수 있습니다.

## 사용하면 안 되는 링크

- Microsoft Learn Plans 링크는 Community Influencer Preferred Visitor 카운트에 사용할 수 없습니다. Learn Plan은 [Community Skiller 가이드](06-community-skiller.md)를 참고하세요.
- 적격 목록에 없는 경로는 Contributor ID를 붙여도 카운트 대상이 아닐 수 있습니다. 공유 전에 [Community Influencer 가이드](05-community-influencer.md)의 최신 적격 URL 목록을 확인하세요.
- 스팸성 클릭 요청, 자동화된 트래픽, Bitly(비틀리)와 같은 제3자 URL 단축기 사용은 피하세요. 공유 콘텐츠는 커뮤니티에 실제로 도움이 되는 설명과 함께 게시해야 합니다.
