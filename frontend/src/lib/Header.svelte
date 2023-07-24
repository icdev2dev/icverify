<script>
    import icverify_logo from '/icverify.jpg'
    let title = "IcVerify"
    let tagLine = "Earn while you help verify replica version builds and decentralize the Internet Computer!!"
</script>


<div id="header">
    <img src={icverify_logo} alt="Logo" id="logo"/>
    <div id="title-tag-container">
        <div id="title">
            {title}
        </div>
        <div id="tag-line">
            {tagLine}
        </div>
    </div>
</div>


<style>

    #header {
        display: flex;
        margin-left: auto;
        margin-right: 0;
        padding: 20px;
        background-color: #f8f9fa;
    }
    #logo {
        height: 80px;
        margin-right: 20px;
    }

    #title {
       margin: 0;
       color: #6c757d;
       font-size: 24px; /* adjust according to your needs */
    }

  #tag-line {
        margin: 0;
        color: #6c757d;
        font-size: 18px; /* adjust according to your needs */
  }
  #title-tag-container {
        display: flex;
        margin-left: 0;
        margin-right: auto;
        flex-direction: column;
        justify-content: space-between;
        height: 80px; /* same as the logo height */
  }

</style>