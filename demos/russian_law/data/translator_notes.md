# Translator Notes - russian_law

## Scope

This entry formalizes an excerpt of Russkaya Pravda as a source-law rule system.
The source is Russian prose; the A4V3 identifiers use ASCII transliteration so
that parser, lint, and cross-run tooling can process the file consistently.

## Modeling Layer

- The IR is source-faithful legal-rule modeling, not a modern legal
  interpretation. Archaic categories such as `Verv`, `Lyudi`, `Chelyadin`,
  `Holop`, `Smerd`, and monetary units are preserved as local ontology sorts.
- Normative effects are mostly encoded as structural predicates such as
  `obyazan_uplatit`, `shtraf`, `vzyiskivaetsya_s`, `zapresheno_*`,
  `razresheno_*`, and `podlezhit_vydache_*` inside constraints. This keeps the
  excerpt close to the article-by-article source structure.
- `Delo` is the local case/event carrier. Most relations include `Delo` as the
  first argument to keep facts scoped to a concrete legal situation and to avoid
  global bare assertions about all people or all things.

## Arity And Role Notes

- Several relations intentionally have arity greater than two because the text
  frequently binds case, actor, victim/recipient, unit, and amount in one legal
  consequence. Future normalization could reify these as payment/penalty
  carrier entities, but the current local IR keeps them as compact frames.
- `obyazan_uplatit(Delo, SubjektPrava, SubjektPrava, DenezhnayaEdinitsa, Plata)`
  roles are `case`, `payer`, `recipient`, `currency_unit`, and `amount`.
- `obyazan_uplatit_bez_poluchatelya(Delo, SubjektPrava, DenezhnayaEdinitsa, Plata)`
  roles are `case`, `payer`, `currency_unit`, and `amount`; the source often
  states only that payment is due without naming a recipient.
- `vzyiskivaetsya_s(Delo, SubjektPrava, DenezhnayaEdinitsa, Plata)` roles are
  `case`, `liable_subject`, `currency_unit`, and `amount`.
- `shtraf(Delo, SubjektPrava, DenezhnayaEdinitsa, Plata)` roles are `case`,
  `liable_subject`, `currency_unit`, and `amount`.
- `plata_za_ubitogo(Delo, Chelovek, DenezhnayaEdinitsa, Plata)` roles are
  `case`, `killed_person`, `currency_unit`, and `amount`.
- `mstit_za_protiv(Delo, Chelovek, Chelovek, Chelovek)` roles are `case`,
  `avenger`, `victim`, and `killer`.
- `rodstvennik(Chelovek, Chelovek, Rodstvo)` roles are `relative`, `anchor`,
  and `kinship_type`.
- `khozyain(Delo, Chelovek, Vesh)` and `sobstvennik(Delo, Chelovek, Vesh)` roles
  are `case`, `owner`, and `thing`.
- `privedeno_svideteley(Delo, Chelovek, Svideteley)` roles are `case`,
  `party`, and `witness_count`.

## Source And Tooling Notes

- The source is Cyrillic; token-level provenance in the current checker is
  mostly Latin/number oriented. For this entry, source phrase coverage and human
  review notes are more meaningful than raw token recall.
- `normalized.md` is intentionally identical to `source.md`; no linguistic
  normalization was applied at this stage.

## Generated Arity Ledger

The following arity > 2 frames are intentionally retained as compact local rule frames. Each line lists the declared argument sorts in order; the first `Delo` argument, when present, is the case/event carrier.
- `rodstvennik` roles by position: arg1 `Chelovek`, arg2 `Chelovek`, arg3 `Rodstvo`.
- `plemyannik_so_storony` roles by position: arg1 `Chelovek`, arg2 `Chelovek`, arg3 `StoronaRodstva`.
- `khozyain` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `sobstvennik` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `ubil` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `nayden_v_vervi` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Verv`.
- `lyudi_ishchut` roles by position: arg1 `Delo`, arg2 `Lyudi`, arg3 `Chelovek`.
- `lyudi_pomogayut_v_uplate` roles by position: arg1 `Delo`, arg2 `Lyudi`, arg3 `Chelovek`.
- `mstit_za_protiv` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`, arg4 `Chelovek`.
- `privedeno_svideteley` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Svideteley`.
- `udarit` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `udarit_orudiem` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`, arg4 `Orudie`.
- `udarit_po` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`, arg4 `ChastCheloveka`.
- `otsechet` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`, arg4 `ChastCheloveka`.
- `vyrvet` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`, arg4 `ChastCheloveka`.
- `obnazhit` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Orudie`.
- `pihnet_ot_sebya` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `pihnet_k_sebe` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `nastignet` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `skroetsya_u` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `vernet_v_techenie_dney` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`, arg4 `Dney`.
- `opoznal_na_tretiy_den` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `razresheno_otobrat_cheloveka` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `poedet_na` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `bez_sprosu` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `ukradet` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `uvesti` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `opoznal_propavshee_v_svoem_miru` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `beret_svoe` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `opoznal_u_kogo_libo` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `zapresheno_otobrat_vesh` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `zapresheno_govorit_eto_moe` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `ukazhet_gde_vzyal` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `yavitsya_na_svod_ne_pozdnee` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Dney`.
- `uznaet_propavshego_chelyadina` roles by position: arg1 `Delo`, arg2 `Gospodin`, arg3 `Chelyadin`.
- `hochet_otnyat` roles by position: arg1 `Delo`, arg2 `Gospodin`, arg3 `Chelyadin`.
- `byl_kuplen_u` roles by position: arg1 `Delo`, arg2 `Chelyadin`, arg3 `Chelovek`.
- `vedet_k` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `otday_chelyadina` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelyadin`.
- `ubezhit_v_horomy_gospodina` roles by position: arg1 `Delo`, arg2 `Holop`, arg3 `Gospodin`.
- `vydaet` roles by position: arg1 `Delo`, arg2 `Gospodin`, arg3 `Holop`.
- `razresheno_uderzhat_cheloveka` roles by position: arg1 `Delo`, arg2 `Gospodin`, arg3 `Chelovek`.
- `razresheno_pobit_gde_zastanet` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `slomaet` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `isportit` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `hochet_uderzhat_u_sebya` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `poluchaet_doplatu_za_porchu` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `otkazyvaetsya_ot_slomannoy_veshi` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `zaplacheno_skolko_dal_pri_pokupke` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `sozhet` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `vykadet` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `samovolnoe_istyazanie` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `istiazanie` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `raspashut` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `srubyat` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Vesh`.
- `privedet_vora` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Chelovek`.
- `ubili_vora_na` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `Mesto`.
- `obyazan_uplatit` roles by position: arg1 `Delo`, arg2 `SubjektPrava`, arg3 `SubjektPrava`, arg4 `DenezhnayaEdinitsa`, arg5 `Plata`.
- `obyazan_uplatit_bez_poluchatelya` roles by position: arg1 `Delo`, arg2 `SubjektPrava`, arg3 `DenezhnayaEdinitsa`, arg4 `Plata`.
- `vzyiskivaetsya_s` roles by position: arg1 `Delo`, arg2 `SubjektPrava`, arg3 `DenezhnayaEdinitsa`, arg4 `Plata`.
- `vzyiskivaetsya_za_vesh` roles by position: arg1 `Delo`, arg2 `Vesh`, arg3 `DenezhnayaEdinitsa`, arg4 `Plata`.
- `shtraf` roles by position: arg1 `Delo`, arg2 `SubjektPrava`, arg3 `DenezhnayaEdinitsa`, arg4 `Plata`.
- `plata_za_ubitogo` roles by position: arg1 `Delo`, arg2 `Chelovek`, arg3 `DenezhnayaEdinitsa`, arg4 `Plata`.
- `plata_lekaryu` roles by position: arg1 `Delo`, arg2 `SubjektPrava`, arg3 `Lekar`.
- `podlezhit_vydache_vesh` roles by position: arg1 `Delo`, arg2 `SubjektPrava`, arg3 `Vesh`.
- `podlezhit_vydache_denezhnoy_sumy` roles by position: arg1 `Delo`, arg2 `SubjektPrava`, arg3 `DenezhnayaEdinitsa`, arg4 `Plata`.
- `kolichestvo_veshi` roles by position: arg1 `Delo`, arg2 `Vesh`, arg3 `Kolichestvo`.
- `sostavit_v_nedelyu` roles by position: arg1 `Delo`, arg2 `DenezhnayaEdinitsa`, arg3 `Plata`.
- `plata_mostnikam` roles by position: arg1 `Delo`, arg2 `Mostnik`, arg3 `DenezhnayaEdinitsa`, arg4 `Plata`.
- `plata_ot_kazhdogo_ustoya` roles by position: arg1 `Delo`, arg2 `Mostnik`, arg3 `Ustoy`, arg4 `DenezhnayaEdinitsa`, arg5 `Plata`.
