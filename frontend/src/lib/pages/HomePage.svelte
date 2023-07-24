<script>
    import { onMount } from 'svelte';
    import jsYaml from 'js-yaml';

    let sections = []

    onMount(async () => {
      // Read the YAML file on component mount
      const response = await fetch('/homepagecontent.yaml');

      const yamlText = await response.text();

      sections = jsYaml.load(yamlText).sections || [];

    });

</script>
<div id="homeheader">
   <table>
      
      {#each sections as section }
      <tr>
        <td><h1> {section.section}</h1></td>
        <td><h2> {section.content}</h2></td>
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
</style>