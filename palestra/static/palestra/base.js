var palestra = {
  init: function() {
    this.init_palestra_pesquisa_form();
  },
  init_palestra_pesquisa_form: function() {
    var filtros = window.document.querySelectorAll('.palestra_pesquisa .avancada'),
      botoes = window.document.querySelectorAll('.palestra_pesquisa .avancado'),
      i,
      filtro;
    for (i = filtros.length; i--;) {
      filtro = filtros[i];
      if (filtro.querySelector('[name=tag]').value === '' &&
          filtro.querySelector('[name=excludetag]').value === '' &&
          filtro.querySelector('[name=palestrante]').value === '') {
        filtro.classList.toggle('hide');
      }
    }
    for (i = botoes.length; i--;) {
      botoes[i].addEventListener('click', this.palestra_pesquisa_form_avancado_toggle);
    }
  },
  palestra_pesquisa_form_avancado_toggle: function(evt) {
    evt.target.parentNode.parentNode.parentNode.querySelector('.avancada').classList.toggle('hide');
  }
};

(function() {
  palestra.init();
}());
