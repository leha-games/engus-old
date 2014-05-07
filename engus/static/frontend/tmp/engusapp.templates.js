angular.module('engusApp').run(['$templateCache', function($templateCache) {
  'use strict';

  $templateCache.put('templates/base.cards.done.html',
    "<div class=\"content\">\n" +
    "    <a ng-click=\"$state.go('base.cards.done.repeat')\" class=\"cards__begin-btn\">\n" +
    "        <i class=\"fa fa-play cards__begin-btn-playbtn\"></i> Начать повторение\n" +
    "    </a>\n" +
    "\n" +
    "    <ul class=\"cards__list\">\n" +
    "        <li class=\"cards__list-item\"\n" +
    "        ng-repeat=\"card in CardsCtrl.getLearned(CardsCtrl.cards)\">\n" +
    "\n" +
    "            <div class=\"cards__list-item-word\"><a class=\"link\" ui-sref=\"base.dictionary.word({ word: card.word })\" ng-bind=\"card.word\"></a></div>\n" +
    "            <div class=\"cards__list-item-buttons\">\n" +
    "                <div class=\"cards__list-item-button cards__list-item-button_type_move\" ng-click=\"CardsCtrl.moveInNew(card)\">В новые</div>\n" +
    "                <div class=\"cards__list-item-button cards__list-item-button_type_remove\" ng-click=\"CardsCtrl.removeCard(card)\">Удалить</div>\n" +
    "            </div>\n" +
    "        </li>\n" +
    "    </ul>\n" +
    "</div>\n"
  );


  $templateCache.put('templates/base.cards.html',
    "<div class=\"submenu__wrapper\">\n" +
    "    <ul class=\"submenu\">\n" +
    "        <li class=\"submenu__item\" ng-class=\"{ active: $state.includes('base.cards.new') }\" ng-click=\"$state.go('base.cards.new')\"><i class=\"fa fa-fw submenu__item-icon\" ng-class=\"{ 'fa-square': $state.includes('base.cards.new'), 'fa-square-o': !$state.includes('base.cards.new') }\"></i> Новые</li>\n" +
    "        <li class=\"submenu__item\" ng-class=\"{ active: $state.includes('base.cards.done') }\" ng-click=\"$state.go('base.cards.done')\"><i class=\"fa fa-fw submenu__item-icon\" ng-class=\"{ 'fa-check-square': $state.includes('base.cards.done'), 'fa-check-square-o': !$state.includes('base.cards.done') }\"></i> Изученные</li>\n" +
    "    </ul>\n" +
    "</div>\n" +
    "<div ui-view>\n" +
    "</div>\n"
  );


  $templateCache.put('templates/base.cards.learning.html',
    "<div class=\"content\">\n" +
    "    <header class=\"learning__word\">\n" +
    "        <h1 class=\"learning__headword\" ng-bind=\"CardsLearningCtrl.current().card.word\"></h1>\n" +
    "        <transcription ng-if=\"CardsLearningCtrl.current().word.transcription\" transcription=\"CardsLearningCtrl.current().word.transcription\" audio-src=\"CardsLearningCtrl.current().word.audio_url\"></transcription>\n" +
    "        <div class=\"learning__card-number\">\n" +
    "            <span class=\"learning__card-number-current\" ng-bind=\"CardsLearningCtrl.cardsToLearn().indexOf(CardsLearningCtrl.current().card) + 1\"></span>/<span ng-bind=\"CardsLearningCtrl.cardsToLearn().length\"></span>\n" +
    "            <i ng-click=\"CardsLearningCtrl.start()\" class=\"fa fa-repeat learning__card-number-reload\"></i>\n" +
    "        </div>\n" +
    "    </header>\n" +
    "    <div class=\"learning__example\" ng-bind=\"CardsLearningCtrl.current().examples.random.text\"></div>\n" +
    "\n" +
    "    <div class=\"learning__btn learning__btn_type_show\" ng-show=\"!(CardsLearningCtrl.current().showDefinitions)\" ng-click=\"CardsLearningCtrl.current().showDefinitions = true\">Показать определение</div>\n" +
    "\n" +
    "    <section class=\"learning__definitions\" ng-if=\"CardsLearningCtrl.current().showDefinitions\">\n" +
    "        <div class=\"dictionary__mueller\" ng-if=\"!CardsLearningCtrl.profile.is_english_mode && !CardsLearningCtrl.current().word.short_definition\" ng-bind-html=\"CardsLearningCtrl.current().word.mueller_definition | mueller\"></div>\n" +
    "        <div class=\"dictionary__short-def\" ng-if=\"!CardsLearningCtrl.profile.is_english_mode && CardsLearningCtrl.current().word.short_definition\" ng-bind=\"CardsLearningCtrl.current().word.short_definition\"></div>\n" +
    "\n" +
    "        <ul class=\"definition__group-list\" ng-if=\"CardsLearningCtrl.profile.is_english_mode || !CardsLearningCtrl.current().word.mueller_definition\">\n" +
    "            <li class=\"definition__group-item\" ng-repeat=\"(groupName, definitionsGroup) in CardsLearningCtrl.current().word.definitionGroups\">\n" +
    "                <h1 class=\"definition__group-name\"><i class=\"fa fa-angle-right definition__group-name-icon\"></i>{{ groupName }}</h1>\n" +
    "                <ol class=\"definition__list\">\n" +
    "                    <li class=\"definition__item\" ng-class=\"{ transparent: ((CardsLearningCtrl.current().examples.length > 0) && (definition.id !== CardsLearningCtrl.current().examples.random.definition)) }\" ng-repeat=\"definition in definitionsGroup | orderBy:'weight'\">\n" +
    "                        <span ng-if=\"CardsLearningCtrl.profile.is_english_mode\" ng-bind=\"definition.definition\"></span>\n" +
    "                        <span ng-if=\"!CardsLearningCtrl.profile.is_english_mode\" ng-bind=\"definition.russian_definition\"></span>\n" +
    "                    </li>\n" +
    "                </ol>\n" +
    "            </li>\n" +
    "        </ul>\n" +
    "    </section>\n" +
    "\n" +
    "    <ul class=\"learning__answer-list\" ng-show=\"!!(CardsLearningCtrl.current().showDefinitions)\">\n" +
    "        <li ng-if=\"!CardsLearningCtrl.current().card.learned\" ng-click=\"CardsLearningCtrl.updateCard(CardsLearningCtrl.current().card, 'get'); CardsLearningCtrl.switchCard();\" class=\"learning__answer-list-item learning__btn learning__btn_type_get\">\n" +
    "            Выучил\n" +
    "        </li>\n" +
    "        <li ng-if=\"CardsLearningCtrl.current().card.learned\" ng-click=\"CardsLearningCtrl.updateCard(CardsLearningCtrl.current().card, 'forget'); CardsLearningCtrl.switchCard();\" class=\"learning__answer-list-item learning__btn learning__btn_type_get\">\n" +
    "            Забыл\n" +
    "        </li>\n" +
    "        <li ng-click=\"CardsLearningCtrl.updateCard(CardsLearningCtrl.current().card, 'good'); CardsLearningCtrl.switchCard();\" class=\"learning__answer-list-item learning__btn learning__btn_type_good\">\n" +
    "            Далее\n" +
    "        </li>\n" +
    "    </ul>\n" +
    "</div>\n"
  );


  $templateCache.put('templates/base.cards.new.html',
    "<div class=\"content\" ui-view>\n" +
    "    <a ng-click=\"$state.go('base.cards.new.learn')\" class=\"cards__begin-btn\">\n" +
    "        <i class=\"fa fa-play cards__begin-btn-playbtn\"></i> Начать изучение\n" +
    "    </a>\n" +
    "\n" +
    "    <ul class=\"cards__list\">\n" +
    "        <li class=\"cards__list-item\"\n" +
    "        ng-repeat=\"card in CardsCtrl.getToLearnNow(CardsCtrl.cards, CardsCtrl.profile)\">\n" +
    "\n" +
    "            <div class=\"cards__list-item-word\"><a class=\"link\" ui-sref=\"base.dictionary.word({ word: card.word })\" ng-bind=\"card.word\"></a></div>\n" +
    "            <div class=\"cards__list-item-buttons\">\n" +
    "                <div class=\"cards__list-item-button cards__list-item-button_type_move\" ng-click=\"CardsCtrl.moveInLearned(card)\">В изученные</div>\n" +
    "                <div class=\"cards__list-item-button cards__list-item-button_type_remove\" ng-click=\"CardsCtrl.removeCard(card)\">Удалить</div>\n" +
    "            </div>\n" +
    "        </li>\n" +
    "\n" +
    "        <li class=\"cards__list-item-after\" ng-if=\"(CardsCtrl.cards | filter: {learned: false}).length > CardsCtrl.profile.learn_by\">Позже</li>\n" +
    "\n" +
    "        <li class=\"cards__list-item\"\n" +
    "        ng-repeat=\"card in CardsCtrl.getToLearnLater(CardsCtrl.cards, CardsCtrl.profile)\">\n" +
    "\n" +
    "            <div class=\"cards__list-item-word\"><a class=\"link\" ui-sref=\"base.dictionary.word({ word: card.word })\" ng-bind=\"card.word\"></a></div>\n" +
    "            <div class=\"cards__list-item-buttons\">\n" +
    "                <div class=\"cards__list-item-button cards__list-item-button_type_move\" ng-click=\"CardsCtrl.moveInLearned(card)\">В изученные</div>\n" +
    "                <div class=\"cards__list-item-button cards__list-item-button_type_remove\" ng-click=\"CardsCtrl.removeCard(card)\">Удалить</div>\n" +
    "            </div>\n" +
    "        </li>\n" +
    "    </ul>\n" +
    "</div>"
  );


  $templateCache.put('templates/base.dictionary.html',
    "<div class=\"content\">\n" +
    "    <section class=\"dictionary\">\n" +
    "        <form class=\"dictionary__search-form\" submit-on=\"submitForm\" ng-submit=\"dict.search(word); dict.word='';\">\n" +
    "            <input \n" +
    "                class=\"dictionary__search-input\" \n" +
    "                type=\"text\" \n" +
    "                autocapitalize=\"none\" \n" +
    "                autocorrect=\"off\"\n" +
    "                autocomplete=\"off\" \n" +
    "                placeholder=\"Поиск слова\" \n" +
    "                blur-on-submit \n" +
    "                ng-model=\"dict.word\" \n" +
    "                ng-focus=\"isFocusOnSearch=true\" \n" +
    "                blur-with-timeout=\"isFocusOnSearch=false\">\n" +
    "            <i class=\"fa fa-refresh fa-spin dictionary__search-input-spinner\" ng-show=\"dict.searching\"></i>\n" +
    "            <ul class=\"dictionary__search-dropdown\" ng-if=\"dict.word && isFocusOnSearch\">\n" +
    "                <li class=\"dictionary__search-dropdown-item\" ng-repeat=\"word in dict.dictionary | filter:dict.word:dict.startsWith | limitTo: 30\">\n" +
    "                    <span class=\"dictionary__search-dropdown-item-link\" ng-click=\"dict.word=word; dict.triggerSubmit(); event.stopPropagation(); \">{{ word }}</span>\n" +
    "                </li>\n" +
    "                <li class=\"dictionary__search-dropdown-item dictionary__search-dropdown-item_state_notfound\" ng-if=\"(dict.dictionary | filter:dict.word:dict.startsWith).length===0\">\n" +
    "                    Слово не найдено\n" +
    "                </li>\n" +
    "            </ul>\n" +
    "        </form>\n" +
    "        <div ui-view>\n" +
    "            <ul class=\"dictionary__word-list\">\n" +
    "                <li class=\"dictionary__word-list-item\" ng-repeat=\"word in dict.dictionary | limitTo:50\">\n" +
    "                    <a class=\"link link_type_block dictionary__word-list-item-link\" ng-class=\"{ last: $last }\" href ui-sref=\"base.dictionary.word({ word: word })\">{{ word }}</a>\n" +
    "                </li>\n" +
    "            </ul>\n" +
    "        </div>\n" +
    "    </section>\n" +
    "</div>\n"
  );


  $templateCache.put('templates/base.dictionary.word.html',
    "<div class=\"dictionary__word\">\n" +
    "    <header class=\"dictionary__word-header\">\n" +
    "        <h1 class=\"dictionary__headword\" ng-bind=\"WordCtrl.rawWord\"></h1>\n" +
    "        <i ng-if=\"WordCtrl.word.word\" ng-click=\"WordCtrl.switchCard()\" class=\"fa dictionary__word-star\" ng-class=\"{ 'fa-star-o': !(WordCtrl.isWordInCards()), 'fa-star active': WordCtrl.isWordInCards() }\"></i>\n" +
    "    </header>\n" +
    "    <transcription ng-if=\"WordCtrl.word.transcription\" transcription=\"WordCtrl.word.transcription\" audio-src=\"WordCtrl.word.audio_url\"></transcription>\n" +
    "\n" +
    "    <section class=\"dictionary__definitions\" ng-if=\"WordCtrl.profile.is_english_mode || (!WordCtrl.profile.is_english_mode && WordCtrl.word.mueller_definition === '') && WordCtrl.word.definition_set\">\n" +
    "        <ul class=\"definition__group-list\">\n" +
    "            <li class=\"definition__group-item\" ng-repeat=\"(groupName, definitionsGroup) in WordCtrl.word.definitionGroups\">\n" +
    "                <h1 class=\"definition__group-name\"><i class=\"fa fa-angle-right definition__group-name-icon\"></i>{{ groupName }}</h1>\n" +
    "                <ol class=\"definition__list\">\n" +
    "                    <li class=\"definition__item\" ng-repeat=\"definition in definitionsGroup | orderBy:'weight'\">\n" +
    "                        <span ng-if=\"WordCtrl.profile.is_english_mode\" ng-bind=\"definition.definition\"></span>\n" +
    "                        <span ng-if=\"!WordCtrl.profile.is_english_mode\" ng-bind=\"definition.russian_definition\"></span>\n" +
    "                        <ul class=\"definition__examples-list\" ng-if=\"(WordCtrl.examples | filter: {definition: definition.id}).length\">\n" +
    "                            <li ng-repeat=\"example in WordCtrl.examples | filter: {definition: definition.id}\">\n" +
    "                                <div class=\"definition__example\" \n" +
    "                                    ng-click=\"!!(example.illustration_url) && (example.showIllustration = true)\"  \n" +
    "                                    ng-hide=\"!!(example.showIllustration)\"\n" +
    "                                    ng-class=\"{ 'with-illustration': example.illustration_url }\" \n" +
    "                                    ng-mouseover=\"exampleHover = true\" \n" +
    "                                    ng-mouseleave=\"exampleHover = false\">\n" +
    "\n" +
    "                                    <span ng-bind-html=\"example.text | markWord:WordCtrl.word.word\"></span>\n" +
    "                                    <i ng-if=\"example.illustration_url\" class=\"fa fa-picture-o definition__example-illustration-icon\" ng-class=\"{ 'hover': exampleHover }\"></i>\n" +
    "                                    <span ng-if=\"!WordCtrl.profile.is_english_mode && example.russian_translation\">— {{ example.russian_translation }}</span>\n" +
    "                                </div>\n" +
    "                                <div ng-if=\"example.illustration_url && example.showIllustration\" ng-click=\"example.showIllustration = false\" class=\"definition__example-with-illustration\">\n" +
    "                                    <img class=\"definition__illustration\" ng-src=\"{{ example.illustration_url }}\">\n" +
    "                                    <div class=\"definition__illustration-text\" ng-bind-html=\"example.text | markWord:WordCtrl.word.word\"></div>\n" +
    "                                </div>\n" +
    "                            </li>\n" +
    "                        </ul>\n" +
    "                    </li>\n" +
    "                </ol>\n" +
    "\n" +
    "            </li>\n" +
    "        </ul>\n" +
    "    </section>\n" +
    "\n" +
    "    <section ng-if=\"!WordCtrl.profile.is_english_mode && WordCtrl.word.mueller_definition\">\n" +
    "        <div class=\"dictionary__mueller\" ng-bind-html=\"WordCtrl.word.mueller_definition | mueller\"></div>\n" +
    "        <ul class=\"definition__examples-list\" ng-if=\"WordCtrl.examples.length\">\n" +
    "            <li ng-repeat=\"example in WordCtrl.examples\">\n" +
    "                <div class=\"definition__example\" \n" +
    "                    ng-click=\"!!(example.illustration_url) && (example.showIllustration = true)\"  \n" +
    "                    ng-hide=\"!!(example.showIllustration)\"\n" +
    "                    ng-class=\"{ 'with-illustration': example.illustration_url }\" \n" +
    "                    ng-mouseover=\"exampleHover = true\" \n" +
    "                    ng-mouseleave=\"exampleHover = false\">\n" +
    "\n" +
    "                    <span ng-bind-html=\"example.text | markWord:WordCtrl.word.word\"></span>\n" +
    "                    <i ng-if=\"example.illustration_url\" class=\"fa fa-picture-o definition__example-illustration-icon\" ng-class=\"{ 'hover': exampleHover }\"></i>\n" +
    "                    <span ng-if=\"example.russian_translation\">— {{ example.russian_translation }}</span>\n" +
    "                </div>\n" +
    "                <div ng-if=\"example.illustration_url && example.showIllustration\" ng-click=\"example.showIllustration = false\" class=\"definition__example-with-illustration\">\n" +
    "                    <img class=\"definition__illustration\" ng-src=\"{{ example.illustration_url }}\">\n" +
    "                    <div class=\"definition__illustration-text\" ng-bind-html=\"example.text | markWord:WordCtrl.word.word\"></div>\n" +
    "                </div>\n" +
    "            </li>\n" +
    "        </ul>\n" +
    "    </section>\n" +
    "\n" +
    "\n" +
    "    <section ng-if=\"WordCtrl.wordNotFound\" class=\"dictionary__word-not-found\">\n" +
    "        Такое слово не найдено\n" +
    "    </section>\n" +
    "</div>\n"
  );


  $templateCache.put('templates/base.html',
    "<div class=\"topmenu\">\n" +
    "    <ul class=\"topmenu__items\">\n" +
    "        <li class=\"topmenu__item\" ng-class=\"{ active: $state.includes('base.dictionary') }\">\n" +
    "            <div class=\"topmenu__item-link\" ng-click=\"$state.go('base.dictionary')\">\n" +
    "                <i class=\"fa fa-book topmenu__item-icon\"></i> \n" +
    "                <span class=\"topmenu__item-text\">Словарь</span>\n" +
    "            </div>\n" +
    "        </li>\n" +
    "        <li class=\"topmenu__item\" ng-class=\"{ active: $state.includes('base.cards') }\">\n" +
    "            <div class=\"topmenu__item-link\" ng-click=\"$state.go('base.cards.new')\">\n" +
    "                <i class=\"fa topmenu__item-icon\" ng-class=\"{ 'fa-star': $state.includes('base.cards'), 'fa-star-o': !$state.includes('base.cards') }\"></i> \n" +
    "                <span class=\"topmenu__item-text\">Карточки</span>\n" +
    "            </div>\n" +
    "        </li>\n" +
    "        <li class=\"topmenu__item\" ng-class=\"{ active: $state.includes('base.profile') }\">\n" +
    "            <div class=\"topmenu__item-link\" ng-click=\"$state.go('base.profile')\">\n" +
    "                <i class=\"fa fa-user topmenu__item-icon\"></i> \n" +
    "                <span class=\"topmenu__item-text\">Профиль</span>\n" +
    "            </div>\n" +
    "        </li>\n" +
    "    </ul>\n" +
    "</div>\n" +
    "<div ui-view></div>\n"
  );


  $templateCache.put('templates/base.profile.html',
    "<div class=\"submenu__wrapper\">\n" +
    "    <ul class=\"submenu\">\n" +
    "        <li class=\"submenu__item\" ng-class=\"{ active: $state.is('base.profile.statistics') }\" ng-click=\"$state.go('base.profile.statistics')\"><i class=\"fa fa-fw fa-bar-chart-o submenu__item-icon\"></i> Статистика</li>\n" +
    "        <li class=\"submenu__item\" ng-class=\"{ active: $state.is('base.profile') }\" ng-click=\"$state.go('base.profile')\"><i class=\"fa fa-fw fa-cog submenu__item-icon\"></i> Настройки</li>\n" +
    "    </ul>\n" +
    "</div>\n" +
    "<div ui-view>\n" +
    "    <div class=\"content\">\n" +
    "        <div class=\"settings__login-as\">\n" +
    "            Вы вошли как <span class=\"settings__username\" ng-bind=\"ProfileCtrl.profile.username\"></span>\n" +
    "            <a class=\"link\" href=\"/accounts/logout/\">Выйти</a><br>\n" +
    "        </div>\n" +
    "        <div class=\"settings__language-mode\">\n" +
    "            Режим словаря:<br>\n" +
    "            <input type=\"radio\" ng-model=\"ProfileCtrl.profile.is_english_mode\" ng-value=\"true\" ng-change=\"ProfileCtrl.saveProfile()\" id=\"is-english-mode\"> <label for=\"is-english-mode\">Английский</label><br>\n" +
    "            <input type=\"radio\" ng-model=\"ProfileCtrl.profile.is_english_mode\" ng-value=\"false\" ng-change=\"ProfileCtrl.saveProfile()\" id=\"is-russian-mode\"> <label for=\"is-russian-mode\">Русский</label>\n" +
    "        </div>\n" +
    "        <div class=\"settings__learn-by\">\n" +
    "            Учить по <input class=\"settings__learn-by-input\" ng-model=\"ProfileCtrl.profile.learn_by\" ng-change=\"ProfileCtrl.saveProfile()\"> <span ng-bind=\"ProfileCtrl.profile.learn_by | declOfNum:['слову', 'слова', 'слов' ]\"></span>\n" +
    "        </div>\n" +
    "    </div>\n" +
    "</div>\n" +
    "\n"
  );


  $templateCache.put('templates/base.profile.statistics.html',
    "<div class=\"content\">\n" +
    "    Изучено слов: {{ ProfileStatisticsCtrl.getLearnedCardsCount() }}<br>\n" +
    "    К изучению: {{ ProfileStatisticsCtrl.getNewCardsCount() }}\n" +
    "</div>"
  );


  $templateCache.put('templates/directives/transcription.html',
    "<div class=\"dictionary__headword-transcription\" ng-class=\"{ 'with-audio': !!(audiosrc) }\" ng-click=\"playTranscription()\" ng-mouseenter=\"transcriptionHover = true\" ng-mouseleave=\"transcriptionHover = false\">\n" +
    "    <span ng-bind=\"transcription\"></span>\n" +
    "    <i ng-if=\"audiosrc\" class=\"fa fa-volume-up dictionary__headword-transcription-audio\" ng-class=\"{ hover: transcriptionHover }\"></i>\n" +
    "    <audio ng-if=\"audiosrc\" id=\"transcription-audio\" preload=\"auto\" ng-src=\"{{ audiosrc }}\" type=\"audio/mpeg\" style=\"height: 0; width: 0;\"></audio>\n" +
    "</div>\n"
  );

}]);
