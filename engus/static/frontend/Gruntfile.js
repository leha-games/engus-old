module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - <%= grunt.template.today("dd-mm-yyyy") %> */\n'
            },
            dist: {
                files: {
                    '../js/engusapp.min.js': [
                        'bower_components/lodash/dist/lodash.compat.min.js',
                        'bower_components/jquery/dist/jquery.min.js',
                        'bower_components/angular/angular.min.js',
                        'bower_components/angular-resource/angular-resource.min.js',
                        'bower_components/angular-ui-router/release/angular-ui-router.min.js',
                        'bower_components/angular-touch/angular-touch.min.js',
                        'engusapp/app.js', 
                        'engusapp/DictionaryCtrl.js', 
                        '<%= ngtemplates.engusApp.dest %>' 
                    ]
                }
            }
        },
        stylus: {
            compile: {
                options: {
                    compress: false
                },
                files: {
                    'tmp/global.stylus.css': 'stylus/global.styl'
                }
            }
        },
        csso: {
            dist: {
                files: {
                    '../css/global.min.css': [
                        'bower_components/font-awesome/css/font-awesome.min.css', 
                        'tmp/global.stylus.css'
                    ]
                }
            }
        },
        ngtemplates: {
            engusApp: {
                cwd: 'engusapp',
                src: 'templates/**/*.html',
                dest: 'tmp/engusapp.templates.js'
            }
        },
        watch: {
            files: ['stylus/*', 'engusapp/**/*'],
            tasks: ['stylus', 'csso', 'ngtemplates', 'uglify']
        }
    });

    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-angular-templates');
    grunt.loadNpmTasks('grunt-csso');

    grunt.registerTask('default', ['ngtemplates', 'uglify', 'stylus', 'csso']);

};
