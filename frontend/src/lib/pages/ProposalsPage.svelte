<script>
    import { onMount } from 'svelte';
    import jsYaml from 'js-yaml';

    let proposals = []

    onMount(async () => {
      // Read the YAML file on component mount
      const response = await fetch('/proposals.yaml');

      const yamlText = await response.text();

      proposals = jsYaml.load(yamlText).proposals || [];

    });

</script>
<div id="homeheader">
   <table>

      <tr>
        <th>Proposal Id </th>
        <th>Revision Id </th>
        <th>Proposal Status </th>
        <th>Sections</th>
        
        
      </tr>
      {#each proposals as proposal }
      <tr>
        <td><h1> {proposal.id}</h1></td>
        <td><h2> {proposal.revisionId}</h2></td>
        <td><h2> {proposal.proposalStatus}</h2></td>
        <td>
            <table>
                <tr>
                    <th>Section</th>
                    <th>Summary</th>
                </tr>
                {#each proposal.sections as section}

                    <tr>
                        <td> {section.section}</td>
                        <td> {section.summary}</td>
                        
                    </tr>
                {/each}
            </table>

        </td>
        
      </tr>
      {/each}
    
   </table>
   
</div>

<style>
        #homeheader {
            margin-left: 0;
            background-color: #f8f9fa;
            color: #6c757d;
            text-align: left;
            
        }
        h1 {
            font-size: 24px;
        }
        h2 {
            font-size: 14px;
        }

          /* Style the table cells (td) */
  td {
    /* Add a border to visually separate cells */
    border: 1px solid #ddd;
    /* Add some padding to make the cells less crowded */
    padding: 8px;
    /* Add vertical alignment to the middle */
    vertical-align: middle;
  }

  /* Style the 'name' column to take up 20% of the width */
  .name {
    width: 40%;
  }

  /* Add a hover effect to rows */
  tr:hover {
    background-color: #ccdeac;
  }
</style>
