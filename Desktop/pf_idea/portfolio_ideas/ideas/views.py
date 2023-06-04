from django.shortcuts import render
import openai

openai.api_key = "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"  # ご自身のAPIキーを設定してください
openai.organization = ""  # ご自身のOrganization IDを設定してください

def def_set(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=1.0,
        max_tokens=100,
        top_p=1.0,
    )
    return response.choices[0].text.strip()

def main_ideas(request):
    if request.method == 'POST':
        answer1 = request.POST['answer1']
        answer2 = request.POST['answer2']
        answer3 = request.POST['answer3']
        answer4 = request.POST['answer4']
        answer5 = request.POST['answer5']
        answer6 = request.POST['answer6']

        prompt = f"{answer1}言語で{answer2}で{answer3}向けの \
        {answer4}なクオリティで{answer5}のようなもので \ {answer6}の要素は除外したポートフォリオを作成ネタを提案してください。"

        portfolio_idea = def_set(prompt)

        return render(request, 'ideas/result.html', {'portfolio_idea': portfolio_idea})
    else:
        return render(request, 'ideas/main_ideas.html')
    
    
    