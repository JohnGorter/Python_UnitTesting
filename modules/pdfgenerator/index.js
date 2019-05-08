'use strict' 
var markdownpdf = require('markdown-pdf')
var foreacher = require('foreacher')
var through = require('through')
var path = require('path')
 
module.exports = (config) =>
  foreacher({source:config, callback:
      (err, files) => { 
         
          try { 
          var targets = files.filter(file => file.indexOf(".md") > 0 && file.indexOf("node_modules") < 0).map(
              // exclude all the node_module stuff
              (file) => "./" + file
          );
          var i = 0; 
          for (let f of targets) {
              console.log("processing: " + path.basename(f));
              markdownpdf({
                preProcessHtml: function(){
                  return through(function(data) {
                          var html =  new Buffer(data).toString('ascii');
                          html = html.replace(new RegExp("<hr>", 'g'),  "<div style=\"page-break-after: always;\"></div>");
                          this.queue(new Buffer(html, 'ascii'));
              })}
          }).concat.from(f).to(config + "/" + path.basename(f, '.md') + ".pdf", function () {
            console.log("Created ./labs.pdf");
            
          });
          i = i + 1;
          }
          } catch(err) {}
      }
  });
