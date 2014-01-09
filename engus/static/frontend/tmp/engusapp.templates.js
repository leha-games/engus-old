angular.module('engusApp').run(['$templateCache', function($templateCache) {
  'use strict';

  $templateCache.put('templates/base.cards.html',
    "<div ui-view>\n" +
    "    <a ui-sref=\"base.cards.learning\" class=\"cards__begin-btn\">\n" +
    "        <span class=\"cards__begin-btn-text\">\n" +
    "            Начать повторение\n" +
    "        </span>\n" +
    "    </a>\n" +
    "    <h1 class=\"cards__table-title\">Мои карточки</h1>\n" +
    "    <table class=\"cards__table\">\n" +
    "        <colgroup>\n" +
    "            <col class=\"cards__table-col-word\">\n" +
    "            <col class=\"cards__table-col-level\">\n" +
    "        <thead>\n" +
    "            <tr>\n" +
    "                <th class=\"cards__table-th\">Слово</th>\n" +
    "                <th class=\"cards__table-th cards__table-level\">Уровень</th>\n" +
    "            </tr>\n" +
    "        </thead>\n" +
    "        <tbody>\n" +
    "            <tr class=\"cards__table-row\" ng-repeat=\"card in CardsCtrl.cards | orderBy:['level', '-created']\">\n" +
    "                <td class=\"cards__table-td\">\n" +
    "                    <a class=\"link\" ui-sref=\"base.dictionary.word({ word: card.word })\" ng-bind=\"card.word\"></a>\n" +
    "                </td>\n" +
    "                <td class=\"cards__table-td cards__table-level\" ng-bind=\"card.level\"></td>\n" +
    "            </tr>\n" +
    "        </tbody>\n" +
    "    </table>\n" +
    "</div>\n"
  );


  $templateCache.put('templates/base.cards.learning.html',
    "<div>\n" +
    "    <header class=\"learning__word\">\n" +
    "        <h1 class=\"learning__headword\" ng-bind=\"CardsLearningCtrl.current.card.word\"></h1>\n" +
    "        <transcription ng-if=\"CardsLearningCtrl.current.word.transcription\" transcription=\"CardsLearningCtrl.current.word.transcription\" audio-src=\"CardsLearningCtrl.current.word.audio_url\"></transcription>\n" +
    "    </header>\n" +
    "    <div class=\"learning__example\" ng-bind=\"CardsLearningCtrl.current.examples.random.text\"></div>\n" +
    "\n" +
    "    <div class=\"learning__btn learning__btn_type_show\" ng-show=\"!(CardsLearningCtrl.current.showDefinitions)\" ng-click=\"CardsLearningCtrl.current.showDefinitions = true\">Показать определение</div>\n" +
    "\n" +
    "    <ul class=\"learning__answer-list\" ng-show=\"!!(CardsLearningCtrl.current.showDefinitions)\">\n" +
    "        <li ng-click=\"CardsLearningCtrl.switchCard('forget')\" class=\"learning__answer-list-item learning__btn learning__btn_type_forget\">\n" +
    "            Забыл\n" +
    "        </li>\n" +
    "        <li ng-click=\"CardsLearningCtrl.switchCard('good')\" class=\"learning__answer-list-item learning__btn learning__btn_type_good\">\n" +
    "            Вспомнил\n" +
    "        </li>\n" +
    "    </ul>\n" +
    "</div>\n"
  );


  $templateCache.put('templates/base.dictionary.html',
    "<section class=\"dictionary\">\n" +
    "    <form class=\"dictionary__search-form\" ng-submit=\"dict.search(word)\">\n" +
    "        <input \n" +
    "            class=\"dictionary__search-input\" \n" +
    "            type=\"text\" \n" +
    "            autocapitalize=\"none\" \n" +
    "            autocorrect=\"off\"\n" +
    "            autocomplete=\"off\" \n" +
    "            placeholder=\"Поиск слова\" \n" +
    "            blur-on-submit ng-model=\"dict.word\" \n" +
    "            ng-focus=\"isFocusOnSearch=true\" \n" +
    "            blur-with-timeout=\"isFocusOnSearch=false\">\n" +
    "        <i class=\"fa fa-refresh fa-spin dictionary__search-input-spinner\" ng-show=\"dict.searching\"></i>\n" +
    "        <ul class=\"dictionary__search-dropdown\" ng-if=\"dict.word && isFocusOnSearch\">\n" +
    "            <li class=\"dictionary__search-dropdown-item\" ng-repeat=\"word in dict.dictionary | filter:dict.word:dict.startsWith | limitTo: 30\">\n" +
    "                <a class=\"dictionary__search-dropdown-item-link\" ui-sref=\"base.dictionary.word({ word: word })\" ng-click=\"dict.word=''; event.stopPropagation()\">{{ word }}</a>\n" +
    "            </li>\n" +
    "            <li class=\"dictionary__search-dropdown-item dictionary__search-dropdown-item_state_notfound\" ng-if=\"(dict.dictionary | filter:dict.word:dict.startsWith).length===0\">\n" +
    "                Слово не найдено\n" +
    "            </li>\n" +
    "        </ul>\n" +
    "    </form>\n" +
    "    <div ui-view>\n" +
    "        <ul class=\"dictionary__word-list\">\n" +
    "            <li class=\"dictionary__word-list-item\" ng-repeat=\"word in dict.dictionary | limitTo:50\">\n" +
    "                <a class=\"link link_type_block dictionary__word-list-item-link\" ng-class=\"{ last: $last }\" href ui-sref=\"base.dictionary.word({ word: word })\">{{ word }}</a>\n" +
    "            </li>\n" +
    "        </ul>\n" +
    "    </div>\n" +
    "</section>\n"
  );


  $templateCache.put('templates/base.dictionary.word.html',
    "<div class=\"dictionary__word\">\n" +
    "    <header class=\"dictionary__word-header\">\n" +
    "        <h1 class=\"dictionary__headword\" ng-bind=\"WordCtrl.rawWord\"></h1>\n" +
    "        <i ng-click=\"WordCtrl.switchCard()\" ng-if=\"WordCtrl.word.word\" class=\"fa dictionary__word-star\" ng-class=\"{ 'fa-star-o': !(WordCtrl.card), 'fa-star active': !!(WordCtrl.card) }\"></i>\n" +
    "        <i ng-if=\"WordCtrl.loading\" class=\"fa fa-cog fa-spin dictionary__word-loading-icon\"></i>\n" +
    "    </header>\n" +
    "    <transcription ng-if=\"WordCtrl.word.transcription\" transcription=\"WordCtrl.word.transcription\" audio-src=\"WordCtrl.word.audio_url\"></transcription>\n" +
    "    <section class=\"dictionary__definitions\" ng-if=\"WordCtrl.word.definition_set\">\n" +
    "        <ul class=\"dictionary__definition-group-list\">\n" +
    "            <li class=\"dictionary__definition-group-item\" ng-repeat=\"(groupName, definitionsGroup) in WordCtrl.word.definitionsGroups\">\n" +
    "                <h1 class=\"dictionary__definition-group-name\"><i class=\"fa fa-angle-right dictionary__definition-group-name-icon\"></i>{{ groupName }}</h1>\n" +
    "                <ol class=\"dictionary__definition-list\">\n" +
    "                    <li class=\"dictionary__definition-item\" ng-repeat=\"definition in definitionsGroup | orderBy:'weight'\">\n" +
    "                        {{ definition.definition }}\n" +
    "                        <ul ng-if=\"(WordCtrl.examples | filter: {definition: definition.id}).length\">\n" +
    "                            <li ng-repeat=\"example in WordCtrl.examples | filter: {definition: definition.id}\">\n" +
    "                                <div class=\"dictionary__definition-example\" \n" +
    "                                    ng-click=\"!!(example.illustration_url) && (example.showIllustration = true)\"  \n" +
    "                                    ng-hide=\"!!(example.showIllustration)\"\n" +
    "                                    ng-class=\"{ 'with-illustration': example.illustration_url }\" \n" +
    "                                    ng-mouseover=\"exampleHover = true\" \n" +
    "                                    ng-mouseleave=\"exampleHover = false\">\n" +
    "\n" +
    "                                    <span ng-bind-html=\"example.text | markWord:WordCtrl.word.word\"></span>\n" +
    "                                    <i ng-if=\"example.illustration_url\" class=\"fa fa-picture-o dictionary__definition-example-illustration-icon\" ng-class=\"{ 'hover': exampleHover }\"></i>\n" +
    "                                    <span ng-if=\"example.russian_translation\">— {{ example.russian_translation }}</span>\n" +
    "                                </div>\n" +
    "                                <div ng-if=\"example.illustration_url && example.showIllustration\" ng-click=\"example.showIllustration = false\" class=\"dictionary__definition-example-with-illustration\">\n" +
    "                                    <img class=\"dictionary__definition-illustration\" ng-src=\"{{ example.illustration_url }}\">\n" +
    "                                    <div class=\"dictionary__definition-illustration-text\" ng-bind-html=\"example.text | markWord:WordCtrl.word.word\"></div>\n" +
    "                                </div>\n" +
    "                            </li>\n" +
    "                        </ul>\n" +
    "                    </li>\n" +
    "                </ol>\n" +
    "\n" +
    "            </li>\n" +
    "        </ul>\n" +
    "    </section>\n" +
    "    <form style=\"display: none;\">\n" +
    "        <div>\n" +
    "            <label for=\"example-definition\">Определение:</label>\n" +
    "            <select if=\"example-definition\" ng-model=\"definition\" ng-options=\"def.definition group by def.part_of_speach for def in WordCtrl.word.definition_set\"></select>\n" +
    "        </div>\n" +
    "        <div>\n" +
    "            <label for=\"example-text\">Пример:</label>\n" +
    "            <textarea id=\"example-text\"></textarea>\n" +
    "        </div>\n" +
    "        <div>\n" +
    "            <label for=\"example-russian-text\">Перевод:</label>\n" +
    "            <textarea id=\"example-russian-text\"></textarea>\n" +
    "        </div>\n" +
    "        <div>\n" +
    "            <label for=\"example-source\">Источник:</label>\n" +
    "            <input id=\"example-source\">\n" +
    "        </div>\n" +
    "        <input type=\"button\" value=\"Отправить\">\n" +
    "    </form>\n" +
    "</div>\n"
  );


  $templateCache.put('templates/base.html',
    "<ul class=\"topmenu\">\n" +
    "    <li class=\"topmenu__item\" ng-class=\"{ active: $state.includes('base.home') }\">\n" +
    "        <a class=\"topmenu__item-link\" ui-sref=\"base.home\"><i class=\"fa fa-home topmenu__item-icon\"></i> Моя страница</a>\n" +
    "    </li>\n" +
    "    <li class=\"topmenu__item\" ng-class=\"{ active: $state.includes('base.dictionary') }\">\n" +
    "        <a class=\"topmenu__item-link\" ui-sref=\"base.dictionary\"><i class=\"fa fa-book topmenu__item-icon\"></i> Словарь</a>\n" +
    "    </li>\n" +
    "    <li class=\"topmenu__item\" ng-class=\"{ active: $state.includes('base.cards') }\">\n" +
    "        <a class=\"topmenu__item-link\" ui-sref=\"base.cards\"><i class=\"fa fa-star-o topmenu__item-icon\"></i> Карточки</a>\n" +
    "    </li>\n" +
    "</ul>\n" +
    "<div class=\"content\" ui-view></div>\n"
  );


  $templateCache.put('templates/directives/transcription.html',
    "<div class=\"dictionary__headword-transcription\" ng-class=\"{ 'with-audio': !!(audiosrc) }\" ng-click=\"playTranscription()\" ng-mouseenter=\"transcriptionHover = true\" ng-mouseleave=\"transcriptionHover = false\">\n" +
    "    <span ng-bind=\"transcription\"></span>\n" +
    "    <span ng-if=\"audiosrc\">\n" +
    "        <i class=\"fa fa-volume-up dictionary__headword-transcription-audio\" ng-class=\"{ hover: transcriptionHover }\"></i>\n" +
    "        <audio id=\"transcription-audio\" preload=\"auto\" ng-src=\"{{ audiosrc }}\" type=\"audio/mpeg\"></audio>\n" +
    "    </span>\n" +
    "</div>\n"
  );

}]);
