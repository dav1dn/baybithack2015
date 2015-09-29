module.exports = function(grunt) {
    
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    grunt.initConfig({
        watch: {
            files: 'bithack/static/css/*.sass',
            tasks: ['sass', 'cssmin']
        },

        sass: {
            build: {
                options: {
                    style: 'expanded'
                },
                files: [{
                    expand: true, // all files in dir
                    cwd: 'bithack/static/css/',
                    src: ['*.sass'],
                    dest: 'bithack/static/css/',
                    ext: '.css'
                }]
            }
        },

        cssmin: {
            build: {
                files: [{
                    expand: true,
                    cwd: 'bithack/static/css/',
                    src: ['*.css', '!*.min.css'],
                    dest: 'bithack/static/css',
                    ext: '.min.css'
                }]
            }
        }
    })
}
