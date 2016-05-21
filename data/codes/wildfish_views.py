from django.core.urlresolvers import reverse_lazyfrom vanilla import ListView, CreateView, DetailView, UpdateView, DeleteViewfrom .forms import {{ cookiecutter.model_name }}Formfrom .models import {{ cookiecutter.model_name }}

class {{ cookiecutter.model_name }}List(ListView):    model = {{ cookiecutter.model_name }}    paginate_by = 20

class {{ cookiecutter.model_name }}Create(CreateView):    model = {{ cookiecutter.model_name }}    form_class = {{ cookiecutter.model_name }}Form    success_url = reverse_lazy('{{ cookiecutter.app_name }}:list')

class {{ cookiecutter.model_name }}Detail(DetailView):    model = {{ cookiecutter.model_name }}

class {{ cookiecutter.model_name }}Update(UpdateView):    model = {{ cookiecutter.model_name }}    form_class = {{ cookiecutter.model_name }}Form    success_url = reverse_lazy('{{ cookiecutter.app_name }}:list')

class {{ cookiecutter.model_name }}Delete(DeleteView):    model = {{ cookiecutter.model_name }}    success_url = reverse_lazy('{{ cookiecutter.app_name }}:list')