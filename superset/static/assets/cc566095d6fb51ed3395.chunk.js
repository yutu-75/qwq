"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[90667],{925550:(t,e,o)=>{o.d(e,{Z:()=>i,g:()=>n});var r=o(205872),l=o.n(r),a=(o(667294),o(435247)),s=o(211965);const i=t=>(0,s.tZ)(a.Z,l()({},t,{css:t=>({".ant-breadcrumb-link":{cursor:"pointer"}})})),n=a.Z.Item},282833:(t,e,o)=>{o.d(e,{Z:()=>s});var r=o(568924),l=o(643048);const a=new r.FilterXSS({whiteList:{...(0,r.getDefaultWhiteList)(),span:["style","class","title"],div:["style","class"],a:["style","class","href","title","target"],img:["style","class","src","alt","title","width","height"],video:["autoplay","controls","loop","preload","src","height","width","muted"]},stripIgnoreTag:!0,css:!1});function s(t,e){return void 0===e||null===e||e instanceof l.Z&&null===e.input?[!1,""]:t?[!1,t(e)]:"string"===typeof e?/<[^>]+>/.test(e)?[!0,a.process(e)]:[!1,e]:[!1,e.toString()]}},643048:(t,e,o)=>{o.d(e,{Z:()=>l});const r=/T(\d{2}:){2}\d{2}$/;class l extends Date{constructor(t,{formatter:e=String,forceUTC:o=!0}={}){let l=t;o&&"string"===typeof l&&r.test(l)&&(l=`${l}Z`),super(l),this.formatter=void 0,this.input=void 0,this.input=t,this.formatter=e,this.toString=()=>this.formatter===String?String(this.input):this.formatter?this.formatter(this):Date.toString.call(this)}}},923694:(t,e,o)=>{function r(t){return"string"===typeof t&&t.length>0&&"%"===t[t.length-1]}function l(t){return r(t)?parseFloat(t)/100:"number"===typeof t?t:parseFloat(t)}o.d(e,{p:()=>l,z:()=>r})},190667:(t,e,o)=>{o.r(e),o.d(e,{default:()=>st});o(150361);var r=o(667294),l=o(828216),a=o(925550),s=o(751995),i=o(455867),n=o(191873),h=o(566342),c=o(767190),p=o(310581),d=o(472813),u=o(45697),g=o.n(u),b=o(923694);const f=function(t){const e={digitsAfterDecimal:2,scaler:1,thousandsSep:",",decimalSep:".",prefix:"",suffix:"",...t};return function(t){if(Number.isNaN(t)||!Number.isFinite(t))return"";const o=function(t,e,o){const r=String(t).split(".");let l=r[0];const a=r.length>1?o+r[1]:"",s=/(\d+)(\d{3})/;for(;s.test(l);)l=l.replace(s,`$1${e}$2`);return l+a}((e.scaler*t).toFixed(e.digitsAfterDecimal),e.thousandsSep,e.decimalSep);return`${e.prefix}${o}${e.suffix}`}},m=/(\d+)|(\D+)/g,y=/\d/,v=/^0/,w=(t,e)=>{if(null!==e&&null===t)return-1;if(null!==t&&null===e)return 1;if("number"===typeof t&&Number.isNaN(t))return-1;if("number"===typeof e&&Number.isNaN(e))return 1;const o=Number(t),r=Number(e);if(o<r)return-1;if(o>r)return 1;if("number"===typeof t&&"number"!==typeof e)return-1;if("number"===typeof e&&"number"!==typeof t)return 1;if("number"===typeof t&&"number"===typeof e)return 0;if(Number.isNaN(r)&&!Number.isNaN(o))return-1;if(Number.isNaN(o)&&!Number.isNaN(r))return 1;let l=String(t),a=String(e);if(l===a)return 0;if(!y.test(l)||!y.test(a))return l>a?1:-1;for(l=l.match(m),a=a.match(m);l.length&&a.length;){const t=l.shift(),e=a.shift();if(t!==e)return y.test(t)&&y.test(e)?t.replace(v,".0")-e.replace(v,".0"):t>e?1:-1}return l.length-a.length},C=function(t){const e={},o={};return t.forEach(((t,r)=>{e[t]=r,"string"===typeof t&&(o[t.toLowerCase()]=r)})),function(t,r){return t in e&&r in e?e[t]-e[r]:t in e?-1:r in e?1:t in o&&r in o?o[t]-o[r]:t in o?-1:r in o?1:w(t,r)}},k=function(t,e){if(t)if("function"===typeof t){const o=t(e);if("function"===typeof o)return o}else if(e in t)return t[e];return w},S=f(),x=f({digitsAfterDecimal:0}),T=f({digitsAfterDecimal:1,scaler:100,suffix:"%"}),$=t=>e=>"string"===typeof e?e:t(e),A={count:(t=x)=>()=>function(){return{count:0,push(){this.count+=1},value(){return this.count},format:t}},uniques:(t,e=x)=>function([o]){return function(){return{uniq:[],push(t){Array.from(this.uniq).includes(t[o])||this.uniq.push(t[o])},value(){return t(this.uniq)},format:$(e),numInputs:"undefined"!==typeof o?0:1}}},sum:(t=S)=>function([e]){return function(){return{sum:0,push(t){Number.isNaN(parseFloat(t[e]))||(0,b.z)(t[e])?this.sum=t[e]:this.sum+=parseFloat(t[e])},value(){return this.sum},format:$(t),numInputs:"undefined"!==typeof e?0:1}}},extremes:(t,e=S)=>function([o]){return function(r){return{val:null,sorter:k("undefined"!==typeof r?r.sorters:null,o),push(e){const r=e[o];if(["min","max"].includes(t)){const e=parseFloat(r);Number.isNaN(e)||(0,b.z)(r)?this.val=!this.val||"min"===t&&r<this.val||"max"===t&&r>this.val?r:this.val:this.val=Math[t](e,null!==this.val?this.val:e)}else("first"===t&&this.sorter(r,null!==this.val?this.val:r)<=0||"last"===t&&this.sorter(r,null!==this.val?this.val:r)>=0)&&(this.val=r)},value(){return this.val},format:t=>"number"===typeof t?e(t):t,numInputs:"undefined"!==typeof o?0:1}}},quantile:(t,e=S)=>function([o]){return function(){return{vals:[],strMap:{},push(t){const e=t[o],r=parseFloat(e);Number.isNaN(r)||(0,b.z)(e)?this.strMap[e]=(this.strMap[e]||0)+1:this.vals.push(r)},value(){if(0===this.vals.length&&0===Object.keys(this.strMap).length)return null;if(Object.keys(this.strMap).length){const t=Object.values(this.strMap).sort(((t,e)=>t-e)),e=Math.floor(t.length/2),o=Object.keys(this.strMap);return o.length%2!==0?o[e]:(o[e-1]+o[e])/2}this.vals.sort(((t,e)=>t-e));const e=(this.vals.length-1)*t;return(this.vals[Math.floor(e)]+this.vals[Math.ceil(e)])/2},format:$(e),numInputs:"undefined"!==typeof o?0:1}}},runningStat:(t="mean",e=1,o=S)=>function([r]){return function(){return{n:0,m:0,s:0,strValue:null,push(t){const e=parseFloat(t[r]);if(Number.isNaN(e)||(0,b.z)(t[r]))return void(this.strValue="string"===typeof t[r]?t[r]:this.strValue);this.n+=1,1===this.n&&(this.m=e);const o=this.m+(e-this.m)/this.n;this.s+=(e-this.m)*(e-o),this.m=o},value(){if(this.strValue)return this.strValue;if("mean"===t)return 0===this.n?NaN:this.m;if(this.n<=e)return 0;switch(t){case"var":return this.s/(this.n-e);case"stdev":return Math.sqrt(this.s/(this.n-e));default:throw new Error("unknown mode for runningStat")}},format:$(o),numInputs:"undefined"!==typeof r?0:1}}},sumOverSum:(t=S)=>function([e,o]){return function(){return{sumNum:0,sumDenom:0,push(t){Number.isNaN(parseFloat(t[e]))||(this.sumNum+=parseFloat(t[e])),Number.isNaN(parseFloat(t[o]))||(this.sumDenom+=parseFloat(t[o]))},value(){return this.sumNum/this.sumDenom},format:t,numInputs:"undefined"!==typeof e&&"undefined"!==typeof o?0:2}}},fractionOf:(t,e="total",o=T)=>(...r)=>function(l,a,s){return{selector:{total:[[],[]],row:[a,[]],col:[[],s]}[e],inner:t(...Array.from(r||[]))(l,a,s),push(t){this.inner.push(t)},format:$(o),value(){const t=l.getAggregator(...Array.from(this.selector||[])).inner.value();return"string"===typeof t?t:this.inner.value()/t},numInputs:t(...Array.from(r||[]))().numInputs}}},N={countUnique:t=>A.uniques((t=>t.length),t),listUnique:(t,e)=>A.uniques((e=>e.join(t)),e||(t=>t)),max:t=>A.extremes("max",t),min:t=>A.extremes("min",t),first:t=>A.extremes("first",t),last:t=>A.extremes("last",t),median:t=>A.quantile(.5,t),average:t=>A.runningStat("mean",1,t),var:(t,e)=>A.runningStat("var",t,e),stdev:(t,e)=>A.runningStat("stdev",t,e)},O={...A,...N},H={Count:(R=O).count(x),"Count Unique Values":R.countUnique(x),"List Unique Values":R.listUnique(", "),Sum:R.sum(S),"Integer Sum":R.sum(x),Average:R.average(S),Median:R.median(S),"Sample Variance":R.var(1,S),"Sample Standard Deviation":R.stdev(1,S),Minimum:R.min(S),Maximum:R.max(S),First:R.first(S),Last:R.last(S),"Sum over Sum":R.sumOverSum(S),"Sum as Fraction of Total":R.fractionOf(R.sum(),"total",T),"Sum as Fraction of Rows":R.fractionOf(R.sum(),"row",T),"Sum as Fraction of Columns":R.fractionOf(R.sum(),"col",T),"Count as Fraction of Total":R.fractionOf(R.count(),"total",T),"Count as Fraction of Rows":R.fractionOf(R.count(),"row",T),"Count as Fraction of Columns":R.fractionOf(R.count(),"col",T)};var R;const F=t=>t.join(String.fromCharCode(0));class M{constructor(t={},e={}){this.props={...M.defaultProps,...t},this.processRecord=this.processRecord.bind(this),g().checkPropTypes(M.propTypes,this.props,"prop","PivotData"),this.aggregator=this.props.aggregatorsFactory(this.props.defaultFormatter)[this.props.aggregatorName](this.props.vals),this.formattedAggregators=this.props.customFormatters&&Object.entries(this.props.customFormatters).reduce(((t,[e,o])=>(t[e]={},Object.entries(o).forEach((([o,r])=>{t[e][o]=this.props.aggregatorsFactory(r)[this.props.aggregatorName](this.props.vals)})),t)),{}),this.tree={},this.rowKeys=[],this.colKeys=[],this.rowTotals={},this.colTotals={},this.allTotal=this.aggregator(this,[],[]),this.subtotals=e,this.sorted=!1,M.forEachRecord(this.props.data,this.processRecord)}getFormattedAggregator(t,e){if(!this.formattedAggregators)return this.aggregator;const[o,r]=Object.entries(t).find((([t,e])=>this.formattedAggregators[t]&&this.formattedAggregators[t][e]))||[];return!o||!r||e&&!e.includes(r)?this.aggregator:this.formattedAggregators[o][r]||this.aggregator}arrSort(t,e,o=!1){const r=t.map((t=>k(this.props.sorters,t)));return function(t,l){const a=Math.min(t.length,l.length);for(let e=0;e<a;e+=1){const a=r[e],s=o?a(l[e],t[e]):a(t[e],l[e]);if(0!==s)return s}return e?t.length-l.length:l.length-t.length}}sortKeys(){if(!this.sorted){this.sorted=!0;const t=(t,e)=>this.getAggregator(t,e).value();switch(this.props.rowOrder){case"key_a_to_z":this.rowKeys.sort(this.arrSort(this.props.rows,this.subtotals.rowPartialOnTop));break;case"key_z_to_a":this.rowKeys.sort(this.arrSort(this.props.rows,this.subtotals.rowPartialOnTop,!0));break;case"value_a_to_z":this.rowKeys.sort(((e,o)=>w(t(e,[]),t(o,[]))));break;case"value_z_to_a":this.rowKeys.sort(((e,o)=>-w(t(e,[]),t(o,[]))))}switch(this.props.colOrder){case"key_a_to_z":this.colKeys.sort(this.arrSort(this.props.cols,this.subtotals.colPartialOnTop));break;case"key_z_to_a":this.colKeys.sort(this.arrSort(this.props.cols,this.subtotals.colPartialOnTop,!0));break;case"value_a_to_z":this.colKeys.sort(((e,o)=>w(t([],e),t([],o))));break;case"value_z_to_a":this.colKeys.sort(((e,o)=>-w(t([],e),t([],o))))}}}getColKeys(){return this.sortKeys(),this.colKeys}getRowKeys(){return this.sortKeys(),this.rowKeys}processRecord(t){const e=[],o=[];this.props.cols.forEach((o=>{e.push(o in t?t[o]:"null")})),this.props.rows.forEach((e=>{o.push(e in t?t[e]:"null")})),this.allTotal.push(t);const r=this.subtotals.rowEnabled?1:Math.max(1,o.length),l=this.subtotals.colEnabled?1:Math.max(1,e.length);let a,s;for(let e=r;e<=o.length;e+=1){a=e<o.length;const r=o.slice(0,e),l=F(r);this.rowTotals[l]||(this.rowKeys.push(r),this.rowTotals[l]=this.getFormattedAggregator(t,o)(this,r,[])),this.rowTotals[l].push(t),this.rowTotals[l].isSubtotal=a}for(let o=l;o<=e.length;o+=1){s=o<e.length;const r=e.slice(0,o),l=F(r);this.colTotals[l]||(this.colKeys.push(r),this.colTotals[l]=this.getFormattedAggregator(t,e)(this,[],r)),this.colTotals[l].push(t),this.colTotals[l].isSubtotal=s}for(let i=r;i<=o.length;i+=1){a=i<o.length;const r=o.slice(0,i),n=F(r);this.tree[n]||(this.tree[n]={});for(let o=l;o<=e.length;o+=1){s=o<e.length;const l=e.slice(0,o),i=F(l);this.tree[n][i]||(this.tree[n][i]=this.getFormattedAggregator(t)(this,r,l)),this.tree[n][i].push(t),this.tree[n][i].isRowSubtotal=a,this.tree[n][i].isColSubtotal=s,this.tree[n][i].isSubtotal=a||s}}}getAggregator(t,e){let o;const r=F(t),l=F(e);return o=0===t.length&&0===e.length?this.allTotal:0===t.length?this.colTotals[l]:0===e.length?this.rowTotals[r]:this.tree[r][l],o||{value:()=>null,format:()=>""}}}M.forEachRecord=function(t,e){if(Array.isArray(t))return t.map((t=>e(t)));throw new Error((0,i.t)("Unknown input format"))},M.defaultProps={aggregators:H,cols:[],rows:[],vals:[],aggregatorName:"Count",sorters:{},rowOrder:"raw",colOrder:"raw"},M.propTypes={data:g().oneOfType([g().array,g().object,g().func]).isRequired,aggregatorName:g().string,cols:g().arrayOf(g().string),rows:g().arrayOf(g().string),vals:g().arrayOf(g().string),valueFilter:g().objectOf(g().objectOf(g().bool)),sorters:g().oneOfType([g().func,g().objectOf(g().func)]),derivedAttributes:g().objectOf(g().func),rowOrder:g().oneOf(["raw","key_a_to_z","key_z_to_a","value_a_to_z","value_z_to_a"]),colOrder:g().oneOf(["raw","key_a_to_z","key_z_to_a","value_a_to_z","value_z_to_a"])};var Z=o(205872),_=o.n(Z),L=(o(717621),o(789549)),z=o(211965);s.iK.div`
  ${({theme:t,isDashboardEditMode:e})=>z.iv`
    table.pvtTable {
      position: ${e?"inherit":"relative"};
      font-size: ${t.typography.sizes.s}px;
      text-align: left;
      border-collapse: separate;
      font-family: ${t.typography.families.sansSerif};
      line-height: 1.4;
      width: 100%;
    }

    table thead {
      position: ${e?"inherit":"sticky"};
      top: 0;
    }

    table tbody tr {
      font-feature-settings: 'tnum' 1;
    }

    table.pvtTable thead tr th,
    table.pvtTable tbody tr th {
      background-color: ${t.colors.grayscale.light5};
      border-top: 1px solid ${t.colors.grayscale.light2};
      border-left: 1px solid ${t.colors.grayscale.light2};
      font-size: ${t.typography.sizes.s}px;
      padding: ${t.gridUnit}px;
      font-weight: ${t.typography.weights.normal};
    }

    table.pvtTable tbody tr.pvtRowTotals {
      position: ${e?"inherit":"sticky"};
      bottom: 0;
    }

    table.pvtTable thead tr:last-of-type th,
    table.pvtTable thead tr:first-of-type th.pvtTotalLabel,
    table.pvtTable thead tr:nth-last-of-type(2) th.pvtColLabel,
    table.pvtTable thead th.pvtSubtotalLabel,
    table.pvtTable tbody tr:last-of-type th,
    table.pvtTable tbody tr:last-of-type td {
      border-bottom: 1px solid ${t.colors.grayscale.light2};
    }

    table.pvtTable
      thead
      tr:last-of-type:not(:only-child)
      th.pvtAxisLabel
      ~ th.pvtColLabel,
    table.pvtTable tbody tr:first-of-type th,
    table.pvtTable tbody tr:first-of-type td {
      border-top: none;
    }

    table.pvtTable tbody tr td:last-of-type,
    table.pvtTable thead tr th:last-of-type:not(.pvtSubtotalLabel) {
      border-right: 1px solid ${t.colors.grayscale.light2};
    }

    table.pvtTable
      thead
      tr:last-of-type:not(:only-child)
      th.pvtAxisLabel
      + .pvtTotalLabel {
      border-right: none;
    }

    table.pvtTable tr th.active {
      background-color: ${t.colors.primary.light3};
    }

    table.pvtTable .pvtTotalLabel {
      text-align: right;
      font-weight: ${t.typography.weights.bold};
    }

    table.pvtTable .pvtSubtotalLabel {
      font-weight: ${t.typography.weights.bold};
    }

    table.pvtTable tbody tr td {
      color: ${t.colors.primary.dark2};
      padding: ${t.gridUnit}px;
      background-color: ${t.colors.grayscale.light5};
      border-top: 1px solid ${t.colors.grayscale.light2};
      border-left: 1px solid ${t.colors.grayscale.light2};
      vertical-align: top;
      text-align: right;
    }

    table.pvtTable tbody tr th.pvtRowLabel {
      vertical-align: baseline;
    }

    table.pvtTable tbody tr th.pvtRowTotalLabel {
      vertical-align: middle;
    }

    .pvtTotal,
    .pvtGrandTotal {
      font-weight: ${t.typography.weights.bold};
    }

    table.pvtTable tbody tr td.pvtRowTotal {
      vertical-align: middle;
    }

    .toggle-wrapper {
      white-space: nowrap;
    }

    .toggle-wrapper > .toggle-val {
      white-space: normal;
    }

    .toggle {
      padding-right: ${t.gridUnit}px;
      cursor: pointer;
    }

    .hoverable:hover {
      background-color: ${t.colors.primary.light4};
      cursor: pointer;
    }
  `}
`;const K="#fafafa",E="#f9f9f9",D=(s.iK.div`
  ${({theme:t})=>z.iv`
    table.pvtTable {
      width: 100%;
      max-width: 100%;
      //
      font-size: ${t.typography.sizes.s}px;
      font-family: ${t.typography.families.sansSerif};
      line-height: 1.4;
      text-align: left;
      position: relative;
      border-collapse: collapse;

      // Cells
      > thead,
      > tbody,
      > tfoot {
        > tr {
          > th,
          > td {
            line-height: 1.4;
            vertical-align: top;
            border-top: 1px solid ${t.colors.grayscale.light2};
            padding: ${t.gridUnit}px;
            font-size: ${t.typography.sizes.s}px;
            font-weight: ${t.typography.weights.normal};
          }
        }
      }

      // Bottom align for column headings
      > thead > tr > th {
        vertical-align: bottom;
        border-bottom: 2px solid ${t.colors.grayscale.light2};
      }

      // Remove top border from thead by default
      > caption + thead,
      > colgroup + thead,
      > thead:first-child {
        > tr:first-child {
          > th,
          > td {
            border-top: 0;
          }
        }
      }

      // .table-head-fixed
      & {
        > thead,
        > tbody > tr.pvtRowTotals {
          position: sticky;
          left: 0;
          z-index: 2;
          background: ${K};
          transition: background 0.3s ease;
        }

        > thead {
          top: 0;
        }

        > tbody > tr.pvtRowTotals {
          bottom: 0;
        }

        > thead > tr,
        > tbody > tr.pvtRowTotals {
          > th,
          > td {
            border: 0 !important;
            // outline-offset: -1px !important;
            outline: 1px solid #e0e0e0 !important;
            color: rgba(0, 0, 0, 0.88);
            font-weight: ${t.typography.weights.bold};
          }
        }
      }

      // .table-bordered
      & {
        border: 1px solid ${t.colors.grayscale.light2};

        > thead,
        > tbody,
        > tfoot {
          > tr {
            > th,
            > td {
              border: 1px solid ${t.colors.grayscale.light2};
            }
          }
        }

        > thead > tr {
          > th,
          > td {
            border-bottom-width: 2px;
          }
        }
      }

      // .table-striped
      // & {
      //   > tbody > tr:nth-of-type(odd) {
      //     background-color: ${E};
      //   }
      // }

      // .table-hover
      & {
        > tbody > tr:hover {
          background-color: ${K};
        }
      }

      tr {
        > th {
          &.active {
            background-color: ${t.colors.primary.light3};
          }
        }
      }

      > tbody > tr {
        > th {
          &.pvtRowLabel {
            vertical-align: baseline;
          }

          &.pvtRowTotalLabel {
            vertical-align: middle;
          }
        }

        > td {
          color: ${t.colors.primary.dark2};

          &.pvtRowTotal {
            vertical-align: middle;
          }
        }
      }

      .pvtTotalLabel {
        font-weight: ${t.typography.weights.bold};
      }

      .pvtSubtotalLabel {
        font-weight: ${t.typography.weights.bold};
      }

      .pvtTotal,
      .pvtGrandTotal {
        font-weight: ${t.typography.weights.bold};
      }

      .toggle-wrapper {
        white-space: nowrap;

        > .toggle-val {
          white-space: normal;
        }
      }

      .toggle {
        padding-right: ${t.gridUnit}px;
        cursor: pointer;
      }

      .hoverable:hover {
        background-color: ${t.colors.primary.light4};
        cursor: pointer;
      }
    }
  `}
`,s.iK.div`
  ${({theme:t})=>z.iv`
    table.pvtTable {
      width: 100%;
      max-width: 100%;
      //
      font-size: ${t.typography.sizes.s}px;
      font-family: ${t.typography.families.sansSerif};
      line-height: 1.4;
      text-align: left;
      position: relative;
      border-collapse: separate;
      border-spacing: 0;

      // Cells
      > thead,
      > tbody,
      > tfoot {
        > tr {
          > th,
          > td {
            line-height: 1.4;
            vertical-align: top;
            border-top: 1px solid ${t.colors.grayscale.light2};
            padding: ${t.gridUnit}px;
            font-size: ${t.typography.sizes.s}px;
            font-weight: ${t.typography.weights.normal};
          }
        }
      }

      // Bottom align for column headings
      > thead > tr > th {
        vertical-align: bottom;
      }

      > thead {
        > tr:last-of-type th,
        > tr:first-of-type th.pvtTotalLabel,
        > tr:nth-last-of-type(2) th.pvtColLabel,
        th.pvtSubtotalLabel {
          border-bottom: 1px solid ${t.colors.grayscale.light2};
        }
      }

      // Remove top border from thead by default
      > caption + thead,
      > colgroup + thead,
      > thead:first-child,
      > tbody {
        > tr:first-child {
          > th,
          > td {
            border-top: 0;
          }
        }
      }

      // .table-head-fixed
      & {
        > thead,
        > tbody > tr.pvtRowTotals {
          position: sticky;
          left: 0;
          z-index: 2;
          background: ${K};
          transition: background 0.3s ease;
        }

        > thead {
          top: 0;
        }

        > tbody > tr.pvtRowTotals {
          bottom: 0;
        }

        > thead > tr,
        > tbody > tr.pvtRowTotals {
          > th,
          > td {
            color: rgba(0, 0, 0, 0.88);
            font-weight: ${t.typography.weights.bold};
          }
        }
      }

      // .table-bordered
      & {
        border: 1px solid ${t.colors.grayscale.light2};

        > thead,
        > tbody,
        > tfoot {
          > tr {
            > th,
            > td {
              border-right: 1px solid ${t.colors.grayscale.light2};
            }
          }
        }

        > thead > tr > th:last-of-type:not(.pvtSubtotalLabel),
        > tbody > tr > td:last-of-type {
          border-right: 0;
        }

        > thead
          > tr:last-of-type:not(:only-child)
          > th.pvtAxisLabel
          + .pvtTotalLabel {
          border-right: 1px solid ${t.colors.grayscale.light2};
        }
      }

      // .table-striped
      // & {
      //   > tbody > tr:nth-of-type(odd) {
      //     background-color: ${E};
      //   }
      // }

      // .table-hover
      & {
        > tbody > tr:hover {
          background-color: ${K};
        }
      }

      tr {
        > th {
          &.active {
            background-color: ${t.colors.primary.light3};
          }
        }
      }

      > tbody > tr {
        > th {
          &.pvtRowLabel {
            vertical-align: baseline;
          }

          &.pvtRowTotalLabel {
            vertical-align: middle;
          }
        }

        > td {
          color: ${t.colors.primary.dark2};

          &.pvtRowTotal {
            vertical-align: middle;
          }
        }
      }

      .pvtTotalLabel {
        font-weight: ${t.typography.weights.bold};
      }

      .pvtSubtotalLabel {
        font-weight: ${t.typography.weights.bold};
      }

      .pvtTotal,
      .pvtGrandTotal {
        font-weight: ${t.typography.weights.bold};
      }

      .toggle-wrapper {
        white-space: nowrap;

        > .toggle-val {
          white-space: normal;
        }
      }

      .toggle {
        padding-right: ${t.gridUnit}px;
        cursor: pointer;
      }

      .hoverable:hover {
        background-color: ${t.colors.primary.light4};
        cursor: pointer;
      }

      .dt-truncate-cell {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      .dt-truncate-cell:hover {
        overflow: visible;
        white-space: normal;
        height: auto;
      }
    }
  `}
`);var P=o(88889),j=o(282833);function q(t,e){const{dataType:o,formatter:r,config:l={}}=t,a=o===P.Z.NUMERIC,s=void 0===l.d3SmallNumberFormat?r:(0,c.JB)(l.d3SmallNumberFormat);return(0,j.Z)(a&&"number"===typeof e&&Math.abs(e)<1?s:r,e)}const V=t=>"number"===typeof t||"string"===typeof t?t:String(t),U=t=>{if(!t)return"none";if("string"==typeof t)return t;const{r:e,g:o,b:r,a:l}=t;return`rgba(${e},${o},${r},${l})`},I={r:255,g:255,b:255,a:1},B={r:0,g:0,b:0,a:.88};function G(t,e,o,r,l){const a=l[r]||r;return t?(0,z.tZ)("span",{className:"toggle-wrapper"},(0,z.tZ)("span",{role:"button",tabIndex:"0",className:"toggle",onClick:o},e),(0,z.tZ)("span",{className:"toggle-val"},V(a))):V(a)}class W extends r.Component{constructor(t){super(t),this.state={collapsedRows:{},collapsedCols:{}},this.clickHeaderHandler=this.clickHeaderHandler.bind(this),this.clickHandler=this.clickHandler.bind(this)}getBasePivotSettings(){const{props:t}=this,e=t.cols,o=t.rows,r={rowTotals:!0,colTotals:!0,...t.tableOptions},l=r.rowTotals||0===e.length,a=r.colTotals||0===o.length,s=t.namesMapping||{},i={arrowCollapsed:"\u25b2",arrowExpanded:"\u25bc",...t.subtotalOptions},n={displayOnTop:!1,enabled:l,hideOnExpand:!1,...i.colSubtotalDisplay},h={displayOnTop:!1,enabled:a,hideOnExpand:!1,...i.rowSubtotalDisplay},c=new M(t,{rowEnabled:h.enabled,colEnabled:n.enabled,rowPartialOnTop:h.displayOnTop,colPartialOnTop:n.displayOnTop}),p=c.getRowKeys(),d=c.getColKeys(),u={},g={},b={};let f=null;r.clickCallback&&(p.forEach((t=>{const e=F(t);e in u||(u[e]={}),d.forEach((o=>{u[e][F(o)]=this.clickHandler(c,t,o)}))})),l&&p.forEach((t=>{g[F(t)]=this.clickHandler(c,t,[])})),a&&d.forEach((t=>{b[F(t)]=this.clickHandler(c,[],t)})),l&&a&&(f=this.clickHandler(c,[],[])));const{tableStyle:m}=t,y={bgColor:m.tableBackground||I,bdColor:m.borderColor||B,opacity:m.opacity},v={fontColor:m.headFontColor||B,fontSize:m.headFontSize||12,lineHeight:m.headLineHeight||24,bgColor:m.headBackground,textAlign:m.headTextAlignment||"left"},w={fontColor:m.tbodyFontColor||B,fontSize:m.tbodyFontSize||12,lineHeight:m.tbodyLineHeight||24,textAlign:m.tbodyTextAlignment||"left"};return{pivotData:c,colAttrs:e,rowAttrs:o,colKeys:d,rowKeys:p,rowTotals:l,colTotals:a,arrowCollapsed:i.arrowCollapsed,arrowExpanded:i.arrowExpanded,colSubtotalDisplay:n,rowSubtotalDisplay:h,cellCallbacks:u,rowTotalCallbacks:g,colTotalCallbacks:b,grandTotalCallback:f,namesMapping:s,tableCss:y,headCss:v,tbodyCss:w}}clickHandler(t,e,o){const r=this.props.cols,l=this.props.rows,a=t.getAggregator(e,o).value(),s={},i=Math.min(r.length,o.length);for(let t=0;t<i;t+=1){const e=r[t];null!==o[t]&&(s[e]=o[t])}const n=Math.min(l.length,e.length);for(let t=0;t<n;t+=1){const o=l[t];null!==e[t]&&(s[o]=e[t])}return e=>this.props.tableOptions.clickCallback(e,a,s,t)}clickHeaderHandler(t,e,o,r,l,a=!1,s=!1){const i={};for(let t=0;t<=r;t+=1){const r=o[t];i[r]=e[t]}return o=>l(o,e[r],i,t,a,s)}collapseAttr(t,e,o){return r=>{r.stopPropagation();const l=e+1,a=o.filter((t=>t.length===l)).map(F),s={};a.forEach((t=>{s[t]=!0})),t?this.setState((t=>({collapsedRows:{...t.collapsedRows,...s}}))):this.setState((t=>({collapsedCols:{...t.collapsedCols,...s}})))}}expandAttr(t,e,o){return r=>{r.stopPropagation();const l={};o.forEach((t=>{for(let o=0;o<=e;o+=1)l[F(t.slice(0,o+1))]=!1})),t?this.setState((t=>({collapsedRows:{...t.collapsedRows,...l}}))):this.setState((t=>({collapsedCols:{...t.collapsedCols,...l}})))}}toggleRowKey(t){return e=>{e.stopPropagation(),this.setState((e=>({collapsedRows:{...e.collapsedRows,[t]:!e.collapsedRows[t]}})))}}toggleColKey(t){return e=>{e.stopPropagation(),this.setState((e=>({collapsedCols:{...e.collapsedCols,[t]:!e.collapsedCols[t]}})))}}calcAttrSpans(t,e){const o=[],r=Array(e).map((()=>0));let l=Array(e).map((()=>null));for(let e=0;e<t.length;e+=1){const a=t[e],s=[];let i=0;const n=Math.min(l.length,a.length);for(;i<n&&l[i]===a[i];)s.push(-1),o[r[i]][i]+=1,i+=1;for(;i<a.length;)r[i]=e,s.push(1),i+=1;o.push(s),l=a}return o}renderColHeaderRow(t,e,o){const{rowAttrs:r,colAttrs:l,colKeys:a,visibleColKeys:s,colAttrSpans:n,rowTotals:h,arrowExpanded:c,arrowCollapsed:p,colSubtotalDisplay:d,maxColVisible:u,pivotData:g,namesMapping:b}=o,{highlightHeaderCellsOnHover:f,omittedHighlightHeaderGroups:m=[],highlightedHeaderCells:y,dateFormatters:v}=this.props.tableOptions,{fontColor:w,fontSize:C,lineHeight:k,textAlign:S}=this.cachedBasePivotSettings.headCss,{bdColor:x}=this.cachedBasePivotSettings.tableCss,T={color:U(w),fontSize:`${C}px`,lineHeight:`${k}px`,textAlign:`${S}`,borderColor:U(x)},{drilldownColumns:$}=this.props,A=0===e&&0!==r.length?(0,z.tZ)("th",{key:"padding",colSpan:r.length,rowSpan:l.length,"aria-hidden":"true",style:T}):null,N=d.enabled&&e!==l.length-1;let O=null,H=null;N&&(O=e+1<u?this.collapseAttr(!1,e,a):this.expandAttr(!1,e,a),H=e+1<u?c:p);const R=(0,z.tZ)("th",{key:"label",className:"pvtAxisLabel text-table-align-style",style:T},G(N,H,O,t,b)),M=[],Z=0!==r.length?1:0;let _=0;for(;_<s.length;){const o=s[_],r=e<o.length?n[_][e]:1;let a="pvtColLabel";if(e<o.length){($&&$.includes(t)||f&&!m.includes(l[e]))&&(a+=" hoverable"),y&&Array.isArray(y[l[e]])&&y[l[e]].includes(o[e])&&(a+=" active");const s=1+(e===l.length-1?Z:0),i=F(o.slice(0,e+1)),n=N?this.toggleColKey(i):null,h=v&&v[t]&&"function"===typeof v[t]?v[t](o[e]):o[e];M.push((0,z.tZ)("th",{className:`${a} text-table-align-style`,key:`colKey-${i}`,colSpan:r,rowSpan:s,onClick:this.clickHeaderHandler(g,o,this.props.cols,e,this.props.tableOptions.clickColumnHeaderCallback),style:T},G(N,this.state.collapsedCols[i]?p:c,n,h,b)))}else if(e===o.length){const t=l.length-o.length+Z;M.push((0,z.tZ)("th",{className:`${a} pvtSubtotalLabel`,key:`colKeyBuffer-${F(o)}`,colSpan:r,rowSpan:t,onClick:this.clickHeaderHandler(g,o,this.props.cols,e,this.props.tableOptions.clickColumnHeaderCallback,!0),style:T},(0,i.t)("Subtotal")))}_+=r}const L=0===e&&h?(0,z.tZ)("th",{key:"total",className:"pvtTotalLabel",rowSpan:l.length+Math.min(r.length,1),onClick:this.clickHeaderHandler(g,[],this.props.cols,e,this.props.tableOptions.clickColumnHeaderCallback,!1,!0),style:T},(0,i.t)("Total (%(aggregatorName)s)",{aggregatorName:(0,i.t)(this.props.aggregatorName)})):null,K=[A,R,...M,L];return(0,z.tZ)("tr",{key:`colAttr-${e}`},K)}renderRowHeaderRow(t){const{rowAttrs:e,colAttrs:o,rowKeys:r,arrowCollapsed:l,arrowExpanded:a,rowSubtotalDisplay:s,maxRowVisible:n,pivotData:h,namesMapping:c}=t,{fontColor:p,fontSize:d,lineHeight:u,textAlign:g}=this.cachedBasePivotSettings.headCss,{bdColor:b}=this.cachedBasePivotSettings.tableCss,f={color:U(p),fontSize:`${d}px`,lineHeight:`${u}px`,textAlign:`${g}`};return(0,z.tZ)("tr",{key:"rowHdr"},e.map(((t,o)=>{const i=s.enabled&&o!==e.length-1;let h=null,p=null;return i&&(h=o+1<n?this.collapseAttr(!0,o,r):this.expandAttr(!0,o,r),p=o+1<n?a:l),(0,z.tZ)("th",{className:"pvtAxisLabel text-table-align-style",key:`rowAttr-${o}`,style:f},G(i,p,h,t,c))})),(0,z.tZ)("th",{className:"pvtTotalLabel",key:"padding",onClick:this.clickHeaderHandler(h,[],this.props.rows,0,this.props.tableOptions.clickRowHeaderCallback,!1,!0),style:f},0===o.length?(0,i.t)("Total (%(aggregatorName)s)",{aggregatorName:(0,i.t)(this.props.aggregatorName)}):null))}renderTableRow(t,e,o){const{rowAttrs:l,colAttrs:a,rowAttrSpans:n,visibleColKeys:h,pivotData:c,rowTotals:p,rowSubtotalDisplay:d,arrowExpanded:u,arrowCollapsed:g,cellCallbacks:b,rowTotalCallbacks:f,namesMapping:m,tbodyCss:y,tableCss:v}=o,{highlightHeaderCellsOnHover:w,omittedHighlightHeaderGroups:C=[],highlightedHeaderCells:k,cellColorFormatters:S,metricColumns:x,dateFormatters:T}=this.props.tableOptions,$={color:U(y.fontColor),fontSize:`${y.fontSize}px`,lineHeight:`${y.lineHeight}px`,textAlign:`${y.textAlign}`,backgroundColor:U(y.bgColor),borderColor:U(v.bdColor)},A=F(t),N=0!==a.length?1:0,O=t.map(((o,r)=>{let a="pvtRowLabel";w&&!C.includes(l[r])&&(a+=" hoverable"),k&&Array.isArray(k[l[r]])&&k[l[r]].includes(o)&&(a+=" active");const s=n[e][r];if(s>0){const e=F(t.slice(0,r+1)),i=1+(r===l.length-1?N:0),n=d.enabled&&r!==l.length-1,h=n?this.toggleRowKey(e):null,p=T&&T[l[r]]?T[l[r]](o):o;return(0,z.tZ)("th",{key:`rowKeyLabel-${r}`,className:`${a} text-table-align-style`,rowSpan:s,colSpan:i,onClick:this.clickHeaderHandler(c,t,this.props.rows,r,this.props.tableOptions.clickRowHeaderCallback),style:$},G(n,this.state.collapsedRows[e]?g:u,h,p,m))}return null})),H=t.length<l.length?(0,z.tZ)("th",{className:"pvtRowLabel pvtSubtotalLabel",key:"rowKeyBuffer",colSpan:l.length-t.length+N,rowSpan:1,onClick:this.clickHeaderHandler(c,t,this.props.rows,t.length,this.props.tableOptions.clickRowHeaderCallback,!0),style:$},(0,i.t)("Subtotal")):null,R=b[A]||{},M=h.map((e=>{const o=F(e),l=c.getAggregator(t,e),a=l.value(),i=[...t,...e];let n,h,p,d;S&&Object.values(S).forEach((t=>{Array.isArray(t)&&i.forEach((e=>{n&&h&&p&&d||t.filter((t=>t.column===e)).forEach((t=>{const e=t.getColorFromValue(a);e&&(n=e.backgroundColor,h=e.color,p=null==e?void 0:e.icon,d=null==e?void 0:e.iconColor)}))}))}));const[u]=x.filter((t=>i.includes(t.key))),{isNumeric:g,config:b={}}=u||{},{truncateLongCells:f}=b,m=Number.isNaN(Number(null==b?void 0:b.columnWidth))?null==b?void 0:b.columnWidth:Number(null==b?void 0:b.columnWidth),y={textAlign:b.horizontalAlign?b.horizontalAlign:g?"right":"left"},[v,w]=q(null!=u?u:{formatter:l.format},a),C=v?{__html:w}:void 0,k=l.isSubtotal?{fontWeight:"bold",...$}:{color:h||$.color,backgroundColor:n||$.backgroundColor,textAlign:y.textAlign,whiteSpace:a instanceof Date?"nowrap":void 0,fontSize:$.fontSize,lineHeight:$.lineHeight,borderColor:$.borderColor},T=(0,s.iK)((({children:r,...l})=>(0,z.tZ)("td",_()({role:"gridcell",className:"pvtVal text-table-align-style",key:`pvtVal-${o}`,onClick:R[o],onContextMenu:o=>this.props.onContextMenu(o,e,t),style:k},l),r)))``,A=(0,z.tZ)("span",{style:{whiteSpace:"nowrap"}},w,p?(0,z.tZ)(r.Fragment,null,"\xa0",(0,z.tZ)(L.k,{type:p,style:{color:d}})):null);return C?f?(0,z.tZ)(T,null,(0,z.tZ)("div",{className:"dt-truncate-cell",style:m?{width:m}:void 0,dangerouslySetInnerHTML:C})):(0,z.tZ)(T,{dangerouslySetInnerHTML:C}):(0,z.tZ)(T,null,f?(0,z.tZ)("div",{className:"dt-truncate-cell",style:m?{width:m}:void 0},A):A)}));let Z=null;if(p){const e=c.getAggregator(t,[]),o=e.value(),[r]=x.filter((e=>t.includes(e.key)));Z=(0,z.tZ)("td",{role:"gridcell",key:"total",className:"pvtTotal text-table-align-style",onClick:f[A],onContextMenu:e=>this.props.onContextMenu(e,void 0,t),style:$},q(null!=r?r:{formatter:e.format},o))}const K=[...O,H,...M,Z];return(0,z.tZ)("tr",{key:`keyRow-${A}`},K)}renderTotalsRow(t){const{rowAttrs:e,colAttrs:o,visibleColKeys:r,rowTotals:l,pivotData:a,colTotalCallbacks:s,grandTotalCallback:n,tbodyCss:h,tableCss:c}=t,p={color:U(h.fontColor),fontSize:`${h.fontSize}px`,lineHeight:`${h.lineHeight}px`,textAlign:`${h.textAlign}`,backgroundColor:U(h.bgColor),borderColor:U(c.bdColor)},{metricColumns:d=[]}=this.props.tableOptions,u=(0,z.tZ)("th",{key:"label",className:"pvtTotalLabel pvtRowTotalLabel",colSpan:e.length+Math.min(o.length,1),onClick:this.clickHeaderHandler(a,[],this.props.rows,0,this.props.tableOptions.clickRowHeaderCallback,!1,!0),style:p},(0,i.t)("Total (%(aggregatorName)s)",{aggregatorName:(0,i.t)(this.props.aggregatorName)})),g=r.map((t=>{const e=F(t),o=a.getAggregator([],t),r=o.value(),[l]=d.filter((e=>t.includes(e.key)));return(0,z.tZ)("td",{role:"gridcell",className:"pvtTotal pvtRowTotal text-table-align-style",key:`total-${e}`,onClick:s[e],onContextMenu:e=>this.props.onContextMenu(e,t,void 0),style:{padding:"5px",...p}},q(null!=l?l:{formatter:o.format},r))}));let b=null;if(l){const t=a.getAggregator([],[]),e=t.value();b=(0,z.tZ)("td",{role:"gridcell",key:"total",className:"pvtGrandTotal pvtRowTotal text-table-align-style",onClick:n,onContextMenu:t=>this.props.onContextMenu(t,void 0,void 0),style:p},t.format(e))}const f=[u,...g,b];return(0,z.tZ)("tr",{key:"total",className:"pvtRowTotals"},f)}visibleKeys(t,e,o,r){return t.filter((t=>!t.some(((o,r)=>e[F(t.slice(0,r))]))&&(t.length===o||F(t)in e||!r.hideOnExpand)))}isDashboardEditMode(){return document.contains(document.querySelector(".dashboard--editing"))}render(){this.cachedProps!==this.props&&(this.cachedProps=this.props,this.cachedBasePivotSettings=this.getBasePivotSettings());const{colAttrs:t,rowAttrs:e,rowKeys:o,colKeys:r,colTotals:l,rowSubtotalDisplay:a,colSubtotalDisplay:s,headCss:i,tableCss:n,tbodyCss:h}=this.cachedBasePivotSettings,c=this.visibleKeys(o,this.state.collapsedRows,e.length,a),p=this.visibleKeys(r,this.state.collapsedCols,t.length,s),d={visibleRowKeys:c,maxRowVisible:Math.max(...c.map((t=>t.length))),visibleColKeys:p,maxColVisible:Math.max(...p.map((t=>t.length))),rowAttrSpans:this.calcAttrSpans(c,e.length),colAttrSpans:this.calcAttrSpans(p,t.length),...this.cachedBasePivotSettings},u={backgroundColor:U(n.bgColor),opacity:`${n.opacity}`,borderColor:U(n.bdColor)},g={backgroundColor:U(i.bgColor)};return(0,z.tZ)(D,{isDashboardEditMode:this.isDashboardEditMode()},(0,z.tZ)("table",{className:"pvtTable",role:"grid",style:u},(0,z.tZ)("thead",{style:g},t.map(((t,e)=>this.renderColHeaderRow(t,e,d))),0!==e.length&&this.renderRowHeaderRow(d)),(0,z.tZ)("tbody",{align:h.textAlign},c.map(((t,e)=>this.renderTableRow(t,e,d))),l&&this.renderTotalsRow(d))))}}W.propTypes={...M.propTypes,tableOptions:g().object,onContextMenu:g().func},W.defaultProps={...M.defaultProps,tableOptions:{}};class J extends r.PureComponent{render(){return(0,z.tZ)(W,this.props)}}J.propTypes=W.propTypes,J.defaultProps=W.defaultProps;const X=J;var Q=o(386769);const Y=s.iK.div`
  ${({height:t,width:e})=>`\n      height: ${t}px;\n      width: ${"string"===typeof e?parseInt(e,10):e}px;\n `}
`,tt=s.iK.div`
  height: 100%;
  overflow: auto;
`,et=(0,i.t)("metric"),ot=["value"],rt=(0,s.iK)(n.default)`
  stroke: ${({theme:t})=>t.colors.grayscale.light2};
  stroke-width: 16px;
`,lt=(0,s.iK)(h.default)`
  stroke: ${({theme:t})=>t.colors.grayscale.light2};
  stroke-width: 16px;
`,at=t=>({Count:O.count(t),"Count Unique Values":O.countUnique(t),"List Unique Values":O.listUnique(", ",t),Sum:O.sum(t),Average:O.average(t),Median:O.median(t),"Sample Variance":O.var(1,t),"Sample Standard Deviation":O.stdev(1,t),Minimum:O.min(t),Maximum:O.max(t),First:O.first(t),Last:O.last(t),"Sum as Fraction of Total":O.fractionOf(O.sum(),"total",t),"Sum as Fraction of Rows":O.fractionOf(O.sum(),"row",t),"Sum as Fraction of Columns":O.fractionOf(O.sum(),"col",t),"Count as Fraction of Total":O.fractionOf(O.count(),"total",t),"Count as Fraction of Rows":O.fractionOf(O.count(),"row",t),"Count as Fraction of Columns":O.fractionOf(O.count(),"col",t)});function st(t){var e;const{data:o,height:s,width:i,groupbyRows:n=[],groupbyColumns:h=[],metrics:u=[],colOrder:g,rowOrder:b,aggregateFunction:f,transposePivot:m,combineMetric:y,rowSubtotalPosition:v,colSubtotalPosition:w,colTotals:k,rowTotals:S,valueFormat:x,emitCrossFilters:T,setDataMask:$,selectedFilters:A,verboseMap:N,columnFormats:O,metricsLayout:H,metricColorFormatters:R,metricColumns:F,dateFormatters:M,onContextMenu:Z,timeGrainSqla:_,drilldownColumns:L,enableDrilldown:K,enableCrossVariable:E,ratioTotals:D,ownState:P,sliceChartId:j,tableStyle:q}=t,{statisticalIndicators:V=[]}=P||{},U=(0,l.v9)((t=>t)),{dataMask:I={}}=U,B=(null==I||null==(e=I[j])?void 0:e.ownState)||{},G=B.columnsFilter||[],W=B.opFilter||[],J=(B.chooseCrossValueList||[]).map((t=>t.value))||[],st=B.statisticalDimension||{};let it=[];null!=st&&st.third_cate_name&&it.push(null==st?void 0:st.third_cate_name);let nt=Array.from(new Set([...n,...G]));E&&it.length&&(nt=Array.from(new Set(it)));const ht=(0,r.useMemo)((()=>(0,c.JB)(x)),[x]),ct=(0,r.useMemo)((()=>Object.entries(O)),[O]),pt=ct.length>0,dt=(0,r.useMemo)((()=>pt?{[et]:Object.fromEntries(ct.map((([t,e])=>[t,(0,c.JB)(e)])))}:void 0),[ct,pt]),ut=(()=>{let t=u.map((t=>"string"===typeof t?t:t.label));if(D||E&&V.includes("total_proportion")){let e=[];u.forEach((t=>{const o="string"===typeof t?t:t.label;e.push(o),e.push(`\u5360\u6bd4(${o})(%)`)})),t=e}return t})(),gt=(0,r.useMemo)((()=>o.reduce(((t,e)=>[...t,...ut.map((t=>({...e,[et]:t,value:e[t]}))).filter((t=>null!==t.value))]),[])),[o,ut]),bt=(0,r.useMemo)((()=>nt.map(p.Z)),[nt]),ft=(0,r.useMemo)((()=>{if(E&&J.length)return J.map(p.Z);return U.sliceEntities.slices[j].form_data.groupbyColumns.map(p.Z)}),[h,J]),mt=(0,r.useMemo)((()=>({[et]:C(ut)})),[ut]),[yt,vt]=(0,r.useMemo)((()=>{let[t,e]=m?[ft,bt]:[bt,ft];return H===Q.Q.ROWS?t=y?[...t,et]:[et,...t]:e=y?[...e,et]:[et,...e],[t,e]}),[y,ft,bt,H,m]),wt=(0,r.useCallback)((t=>{const e=Object.keys(t);let o=[...nt,...h];E&&J.length&&(o=J),$({extraFormData:{filters:0===e.length?void 0:e.map((e=>{var r;const l=null==t?void 0:t[e],a=null!=(r=o.find((t=>(0,d.s9)(t)?t===e:!!(0,d.GA)(t)&&t.label===e)))?r:"";return null===l||void 0===l?{col:a,op:"IS NULL"}:{col:a,op:"IN",val:l}}))},filterState:{value:t&&Object.keys(t).length?Object.values(t):null,selectedFilters:t&&Object.keys(t).length?t:null}})}),[h,nt,$,J]),Ct=t=>{const e={...t},o=Object.keys(e);if(o.length>=L.length)return;if(o.filter(((t,e)=>t!==L[e])).length)return void $({ownState:{}});const r=o.map((e=>({col:e,op:"==",val:t[e]})));o.push(L[o.length]);$({ownState:{opFilter:r,columnsFilter:o}})},kt=(0,r.useCallback)(((t,e,o,r,l,a)=>{if(K)return void Ct(o);if(l||a||!T)return;const s={...o};delete s[et];const i=Object.entries(s);if(0===i.length)return;const[n,h]=i[i.length-1];let c={...A||{}};c=A&&((t,e)=>{var o;return!!A&&(null==(o=A[t])?void 0:o.includes(e))})(n,h)?{}:{[n]:[h]},Array.isArray(c[n])&&0===c[n].length&&delete c[n],wt(c)}),[T,A,wt]),St=(0,r.useMemo)((()=>({clickRowHeaderCallback:kt,clickColumnHeaderCallback:kt,colTotals:k,rowTotals:S,highlightHeaderCellsOnHover:T,highlightedHeaderCells:A,omittedHighlightHeaderGroups:[et],cellColorFormatters:{[et]:R},metricColumns:F,dateFormatters:M})),[k,M,T,F,R,S,A,kt]),xt=(0,r.useMemo)((()=>({colSubtotalDisplay:{displayOnTop:w},rowSubtotalDisplay:{displayOnTop:v},arrowCollapsed:(0,z.tZ)(rt,null),arrowExpanded:(0,z.tZ)(lt,null)})),[w,v]),Tt=(0,r.useCallback)(((t,e,o)=>{if(Z){t.preventDefault(),t.stopPropagation();const r=[];e&&e.length>1&&e.forEach(((t,e)=>{const o=vt[e],l=M[o],a=(null==l?void 0:l(t))||String(t);e>0&&r.push({col:o,op:"==",val:t,formattedVal:a,grain:l?_:void 0})})),o&&o.forEach(((t,e)=>{const o=yt[e],l=M[o],a=(null==l?void 0:l(t))||String(t);r.push({col:o,op:"==",val:t,formattedVal:a,grain:l?_:void 0})})),Z(t.clientX,t.clientY,r)}}),[vt,M,Z,yt,_]);return(0,z.tZ)(Y,{height:s,width:i},(0,z.tZ)(tt,null,W.length>0&&(0,z.tZ)(a.Z,null,(0,z.tZ)(a.g,{onClick:()=>{$({ownState:{}})}},"\u5168\u90e8"),W.map(((t,e)=>(0,z.tZ)(a.g,{onClick:()=>{((t,e)=>{const o={};W.filter(((t,o)=>o<=e)).forEach((t=>{o[null==t?void 0:t.col]=null==t?void 0:t.val})),Ct(o)})(0,e)}},null==t?void 0:t.val)))),(0,z.tZ)(X,{data:gt,rows:yt,cols:vt,aggregatorsFactory:at,defaultFormatter:ht,customFormatters:dt,aggregatorName:f,vals:ot,colOrder:g,rowOrder:b,sorters:mt,tableOptions:St,subtotalOptions:xt,namesMapping:N,onContextMenu:Tt,drilldownColumns:L,tableStyle:q})))}}}]);