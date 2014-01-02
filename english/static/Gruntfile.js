module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            options: {
                separator: ';\n'
            },
            dist: {
                src: [
                    'js/lib/underscore.min.js',
                    'js/lib/angular.min.js',
                    'js/lib/angular-resource.min.js',
                    'js/lib/angular-ui-router.min.js',
                    'js/app/app.js', 
                    'js/app/DictionaryCtrl.js', 
                    '<%= ngtemplates.engusApp.dest %>' 
                ],
                dest: 'dist/js/app.js'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= grunt.template.today("dd-mm-yyyy") %> */\n'
            },
            dist: {
                files: {
                    'dist/js/app.min.js': ['<%= concat.dist.dest %>']
                }
            }
        },
        stylus: {
            compile: {
                options: {
                    compress: false
                },
                files: {
                    'dist/css/app.css': 'styl/global.styl'
                }
            }
        },
        csso: {
            dist: {
                files: {
                    'dist/css/app.min.css': ['css/font-awesome-4.0.3/css/font-awesome.min.css', 'dist/css/app.css']
                }
            }
        },
        ngtemplates: {
            engusApp: {
                cwd: 'js/app',
                src: 'templates/**/*.html',
                dest: 'dist/js/engus.templates.js'
            }
        },
        watch: {
            files: ['styl/*', 'js/app/templates/**/*.html'],
            tasks: ['stylus', 'csso', 'ngtemplates']
        }
    });

    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-angular-templates');
    grunt.loadNpmTasks('grunt-csso');

    grunt.registerTask('default', ['ngtemplates', 'concat', 'uglify', 'stylus', 'csso']);

};
