<script>
  import { currentLang } from '$lib/stores'
  let lang = 'en'
  $: {
    currentLang.set(lang)
  }
</script>

<div class="language" role="radiogroup" aria-labelledby="language-switcher1">
  <div class="language__container--left language__container--fr">
    <input
      class="language__control"
      bind:group={lang}
      type="radio"
      id="language1-1"
      name="language-switch1"
      value="fr"
    />
    <label class="language__label" for="language1-1" />
  </div>
  <div class="language__container--right language__container--en">
    <input
      class="language__control"
      bind:group={lang}
      type="radio"
      id="language1-2"
      name="language-switch1"
      value="en"
    />
    <label class="language__label" for="language1-2" />
  </div>
</div>

<style lang="scss">
  // language variables

  $language-width: 30px;
  $language-height: 30px;
  $language-focus: #85bffd;
  $language-border: #ccc;
  $language-hover: #eee;
  $language-checked: #ddd;

  // language styles

  .language {
    width: $language-width * 2;
    height: $language-height;
    font-size: 1rem;
    line-height: 1;
    display: flex;
    @include mobile {
      margin-left: auto;
    }
    margin-right: 1rem;
  }

  .language__container--left,
  .language__container--right {
    position: relative;
    float: left;
    width: $language-width;
    height: $language-height;
  }

  .language__label {
    position: absolute;
    top: 0;
    left: 0;
    width: $language-width;
    height: $language-height;
    border: 1px solid $language-border;
    padding: 7px 8px 5px 0;
    background-color: white;
    background-repeat: no-repeat;
    background-position: 7px 7px;
    background-size: 14px;
    text-align: right;
    text-transform: uppercase;
    cursor: pointer;
  }

  .language__container--left .language__label {
    border-radius: 4px 0 0 4px;
  }

  .language__container--right .language__label {
    border-left: 0;
    border-radius: 0 4px 4px 0;
  }

  .language__control:hover + .language__label,
  .language__control:focus + .language__label {
    background-color: $language-hover;
  }

  .language__control:checked + .language__label {
    background-color: $language-checked;
  }

  .language__control:focus + .language__label,
  .language__control:checked:focus + .language__label {
    z-index: 2;
    outline: 2px solid $language-focus;
    box-shadow: 0 0 8px $language-focus;
  }

  // country flags

  .language__container--fr .language__label {
    background-image: url('$lib/assets/fr.svg');
  }

  .language__container--en .language__label {
    background-image: url('$lib/assets/gb.svg');
  }
</style>
