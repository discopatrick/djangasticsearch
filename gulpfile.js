var gulp = require('gulp');
var less = require('gulp-less');
var shell = require('gulp-shell')
var path = require('path');

gulp.task('default', function() {
  // default task
});

gulp.task('less', function() {
  return gulp.src('./less/**/*.less')
    .pipe(less())
    .pipe(gulp.dest('./djangasticsearch/djangasticsearch/static/css/'))
    .pipe(shell('cd djangasticsearch && ../venv/bin/python manage.py collectstatic --noinput'));
});

gulp.watch('./less/**/*.less', ['less']);
