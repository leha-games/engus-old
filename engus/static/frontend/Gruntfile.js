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
                        'bower_components/angular/angular.min.js',
                        'bower_components/angular-resource/angular-resource.min.js',
                        'bower_components/angular-ui-router/release/angular-ui-router.min.js',
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
                    'tmp/engusapp.stylus.css': 'styl/global.styl'
                }
            }
        },
        csso: {
            dist: {
                files: {
                    '../css/engusapp.min.css': [
                        'bower_components/font-awesome/css/font-awesome.min.css', 
                        'tmp/engusapp.stylus.css'
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
            files: ['styl/*', 'engusapp/templates/**/*.html'],
            tasks: ['stylus', 'csso', 'ngtemplates']
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
