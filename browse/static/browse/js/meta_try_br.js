var table = $('#table').DataTable({
        fixedColumns: {
          left: 1
      },
      pageLength : 10,
      lengthMenu: [[10, 20, 50], [10, 20, 50]],
      "bPaginate": true, //
      "bAutoWidth": false,

	  	//"searching": false, //
	  	"info":	true, //
	     "fixedHeader": true, //
       "bFilter": true,
       "bProcessing": true,
       "columnDefs": [
       {
        "targets": 0,
        "data": 6,
        "render": function(data,type,full) {
                   return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/" + data+'">' + full[0] +"</a>";
        },

      },
      {
                 "targets": [6],
                 "visible": false,
             },],

             buttons: [
                   {
                           extend: 'print',
                           text: 'Print all',
                             exportOptions: {
                                 modifier: {
                                   selected: null
                             }
                         }
                     },
                 {
                     extend: 'print',
                     text: 'Print selected'
                 }
             ],
             select: true,

             "dom": 'Brtlip'
});
