'use strict'
let fs = require('fs');
let recursive = require('recursive-readdir');


module.exports = (config)=>{
    readconfig(config).then(
        (options) => 
          recursive(config.source, config.callback)
         //  fs.readdir(options.source , options.callback)
    );
}
function readconfig(configfilename){
    return new Promise(function(resolve, reject){
        
          var configfile = {};
          if (typeof configfilename === 'object') configfile = configfilename;
          if (typeof configfilename  === 'string') configfile = JSON.parse(configfilename);
        //  if (typeof configfile  === 'string') configfile = JSON.parse(fs.readFileSync('./' + configfilename));
          resolve({
             source : configfile.source || './',
             callback : configfile.callback || ((err, res) => console.log(res))
          });
    });
}