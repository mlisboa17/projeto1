from django.shortcuts import render,redirect
from .models import Transacao

# Create your views here.
def menu(request):
    if request.method == 'POST':
        # Verifica se o usuario quer deletar
        delete_id = request.POST.get('delete_id')
        if delete_id:
            Transacao.objects.filter(id=delete_id).delete()
            return redirect('/') # Redireciona para a mesma pagina apos deletar
        
        # Caso contrario, adiciona uma nova transacao
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        tipo = request.POST.get('tipo')
        if descricao and valor and tipo:
            Transacao.objects.create(descricao=descricao, valor=valor, tipo=tipo)
            return redirect('/') # Redireciona para a mesma pagina apos adicionar
    
    # Exibe os dados (para GET e POST)
    transacoes = Transacao.objects.all()
    total_receitas = sum(t.valor for t in transacoes if t.tipo == 'R')
    total_despesas = sum(t.valor for t in transacoes if t.tipo == 'D')
    saldo = total_receitas - total_despesas

    return render(request, 'home.html', {
        'transacoes': transacoes,
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo
    })


        