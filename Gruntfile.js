module.exports = function(grunt) {
    
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    grunt.initConfig({
        watch: {
            files: ['sass/*.scss'],
            tasks: ['sass', 'cssmin']
        },

        sass: {
            build: {
                options: {
                    style: 'expanded',
                    lineNumbers: true,
                    sourcemap: 'none',
                    loadPath: require('node-neat').includePaths,
                },
                files: [{
                    expand: true, // all files in dir
                    cwd: 'sass/',
                    src: ['*.scss'],
                    dest: 'css/',
                    ext: '.css'
                }]
            }
        },

        cssmin: {
            build: {
                files: [{
                    expand: true,
                    cwd: 'css/',
                    src: ['*.css', '!*.min.css'],
                    dest: 'css/',
                    ext: '.min.css'
                }]
            }
        }
    })

    grunt.registerTask('default', ['sass', 'cssmin']);
}
