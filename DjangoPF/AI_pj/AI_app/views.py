from django.shortcuts import render
import openai

def def_set(prompt):
    # OpenAIの処理
    openai.api_key = ""  
    openai.organization = "" 

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=1.0,
        max_tokens=100,
        top_p=1.0,
    )
    return response.choices[0].text.strip()

def index(request):
    if request.method == 'POST':
        answer1 = request.POST.get('answer1')
        answer2 = request.POST.get('answer2')
        answer3 = request.POST.get('answer3')
        answer4 = request.POST.get('answer4')
        answer5 = request.POST.get('answer5')
        answer6 = request.POST.get('answer6')
        
        prompt = f"{answer1}言語で{answer2}で{answer3}向けの{answer4}なクオリティで{answer5}のようなもので{answer6}の要素は除外したポートフォリオ作成ネタを提案してください"
        
        portfolio_idea = def_set(prompt)

        return render(request, 'index2.html', {'portfolio_idea': portfolio_idea})

    return render(request, 'index.html')